from django.shortcuts import render, redirect, get_object_or_404
from .models import VisitorRecord, Market, Review, Openhour, Store, Item
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from datetime import datetime
from .serializers import MarketSerializer, ReviewSerializer, ReviewUpdateSerializer, ItemSerializer, ItemUpdateSerializer, StoreSerializer, StoreUpdateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from qr_code.qrcode.utils import ContactDetail, QRCodeOptions
from django.contrib.auth import get_user_model
import qrcode
from django.template import RequestContext, Template, Context
import qrcode.image.svg
import requests
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from accounts.models import User 

User = get_user_model()


# market 관련 api
@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)

# qrcode 보여주는 api
@api_view(['GET'])
@permission_classes([AllowAny])
def qrcode_page(request, market_pk, user_pk):
    user_id = get_object_or_404(User, pk=user_pk)
    market_id = get_object_or_404(Market, pk=market_pk)
    time = datetime.now()

    contact_detail = ContactDetail(
        user_id=user_id.pk,
        market_id=market_id.pk,
        time=time,
    )
    print(contact_detail)

    year = str(time.year)
    month = str(time.month)
    day = str(time.day)
    hour = str(time.hour)
    time_str = year+month+day+hour

    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(contact_detail, image_factory=factory)
    img_save = img.save(f'market/images/{user_id}{market_id}{time_str}.png')
    print('png_done')

    return HttpResponse(img_save, content_type="image/png")

def go(request):
    url = "http://127.0.0.1:8000/market/qrcode_page/1/1/"
    response = requests.get(url=url)
    print('response.text')
    print(response.text)

    return response

# visitorRecord에 저장하기
@api_view(['GET'])
@permission_classes([AllowAny])
def save_visitor(request, market_pk, user_pk):
    # user = get_object_or_404(User, pk=user_pk)
    # market = get_object_or_404(Market, pk=market_pk)
    time = datetime.now()

    # print('user.id')
    # print(user.id)
    visitor_record = VisitorRecord()
    visitor_record.user_id=user_pk
    visitor_record.date=time
    visitor_record.markets_id=market_pk
    visitor_record.save()

    return Response({'message': 'VisitoRecord is successfully saved'})


# 리뷰 하나 쓰기
@api_view(['POST'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def write_review(request, market_pk):
    title = request.data.get('title')
    content = request.data.get('content')
    image = request.data.get('image')
    score = request.data.get('score')
    user_id = request.data.get('user_id')
    market = get_object_or_404(Market, pk=market_pk)
    user =  get_object_or_404(User, pk=user_id)
    review = Review()
    review.market = market
    review.title = title
    review.content = content
    review.image = image
    review.score = score
    review.user = user
    review.save()
    serializer = ReviewSerializer(instance = review)
    return Response(serializer.data)

# 특정 리뷰 한개 가져오기
@api_view(['GET'])
@permission_classes([AllowAny])
def get_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

# market_pk에 따라서 시장 하나에 딸린 모든 리뷰 가져오기
@api_view(['GET'])
@permission_classes([AllowAny])
def market_reviews(request, market_pk):
    reviews = Review.objects.all().filter(market=market_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 리뷰 한 개 수정 혹은 삭제하기
@api_view(['PUT','DELETE'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def ud_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "PUT":
        serializer = ReviewUpdateSerializer(
            data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            Response({'message': 'put error'})
    else:
        review.delete()
        return Response({'message': 'Review is successfully deleted'})


'''여기는 상점 관련'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def write_store(request, market_pk):
    serializer = StoreSerializer(data = request.data)
    market = get_object_or_404(Market, pk=market_pk)
    if serializer.is_valid(raise_exception=True):
        serializer.save(market_id = market_pk)
    return Response(serializer.data)

# 특정 상점 한개 가져오기
@api_view(['GET'])
@permission_classes([AllowAny])
def get_store(request, store_pk):
    store = get_object_or_404(Store, pk=store_pk)
    serializer = StoreSerializer(store)
    return Response(serializer.data)


# market_pk에 따라서 시장 하나에 딸린 모든 상점들 가져오기
@api_view(['GET'])
@permission_classes([AllowAny])
def market_stores(request, market_pk):
    stores = Store.objects.all().filter(market=market_pk)
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


# 상점 한 개 수정 혹은 삭제하기
@api_view(['PUT','DELETE'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def ud_store(request, store_pk):
    store = get_object_or_404(Store, pk=store_pk)
    if request.method == "PUT":
        serializer = StoreUpdateSerializer(
            data=request.data, instance=store)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            Response({'message': 'put error'})
    else:
        store.delete()
        return Response({'message': 'Store is successfully deleted'})
    
'''여기는 물품 관련'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def write_item(request, store_pk):
    serializer = ItemSerializer(data = request.data)
    store = get_object_or_404(Store, pk=store_pk)
    if serializer.is_valid(raise_exception=True):
        serializer.save(store_id = store_pk)
    return Response(serializer.data)

# store_pk에 따라서 가게 하나에 딸린 모든 물품 가져오기
@api_view(['GET'])
@permission_classes([AllowAny])
def store_items(request, store_pk):
    items = Item.objects.all().filter(store=store_pk)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# 물품 한개 수정 혹은 삭제
@api_view(['PUT','DELETE'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def ud_item(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if request.method == "PUT":
        serializer = ItemUpdateSerializer(
            data=request.data, instance=item)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            Response({'message': 'put error'})
    else:
        item.delete()
        return Response({'message': 'Item is successfully deleted'})
