from django.shortcuts import render, redirect, get_object_or_404
from .models import VisitoRecord, Market, Review, Openhour, File
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from datetime import datetime
from .serializers import MarketSerializer, VisitorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from qr_code.qrcode.utils import ContactDetail, QRCodeOptions
from django.contrib.auth import get_user_model
import qrcode
# from PIL import Image
from django.http import FileResponse
from qrcode.image.pure import PymagingImage

User = get_user_model()

# market 관련 api
@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)


# VisitorRecord 정보 저장 api
@api_view(['POST'])
@permission_classes([AllowAny])
def make_visitor_record(request, market_pk):
    serializer = VisitorSerializer(data = request.data)
    user_id = request.data.get('user_id')
    if serializer.is_valid(raise_exception=True):
        serializer.save(market = market_pk)
    return Response(serializer.data)


# Visitor 정보 저장 api
@api_view(['POST'])
@permission_classes([AllowAny])
def makevisitor(request):
    serializer = VisitorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return HttpResponse('Sucess Visitor')

# # qrcode그림 보내기
# def send_file(response):
#     img = open('images/{}.jpg', 'rb')
#     response = FileResponse(img)
#     return response


# qrcode 보여주는 api
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def qrcode_page(request, market_pk, user_pk):
    user_id = get_object_or_404(User, pk=user_pk)
    market_id = get_object_or_404(Market, pk=market_pk)
    time = datetime.now()
    dataaa = dict(user_id=user_id, time=time)

    contact_detail = dict(
        user_id=user_id,
        market_id=market_id,
        time=time,
    )

    # contact_detail.pro

    options = QRCodeOptions(size='t', border=6, error_correction='L')

    # img = qrcode.make(contact_detail)
    # pic=img.save(f'{user_id}.png')
    # pic=Image.open()

    # layout = File()
    # layout.image = f'{user_id}.png'
    # layout.save('pic')

    # file = File.objects.get(name='57 Chevy')

    # print(context)

    img = qrcode.make(contact_detail, image_factory=PymagingImage)
    img.save(f'market/images/{user_id}.png')
    response = FileResponse(open(f'{user_id}.png', 'rb'))
    context = dict(
        response=response
    )
    # context = dict(img=img
    # )
    # url_string = str(request.get_host())
    # print('url_string')
    # print(url_string)
    return JsonResponse(context)
    # return render(request, 'market/qrcode_page.html', context=context)
    # return render(request, 'market/qrcode_page.html', img=img)
