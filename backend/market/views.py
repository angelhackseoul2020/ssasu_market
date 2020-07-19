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
# from qrcode.image.pure import PymagingImage
from django.template import RequestContext, Template, Context
import qrcode.image.svg
import requests
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

User = get_user_model()

# market 관련 api
@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)


# # VisitorRecord 정보 저장 api
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def make_visitor_record(request, market_pk):
#     serializer = VisitorSerializer(data = request.data)
#     user_id = request.data.get('user_id')
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(market = market_pk)
#     return Response(serializer.data)


# Visitor 정보 저장 api
@api_view(['POST'])
@permission_classes([AllowAny])
def makevisitor(request):
    serializer = VisitorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return HttpResponse('Sucess Visitor')

# qrcode 보여주는 api
@api_view(['GET'])
@permission_classes([AllowAny])
def qrcode_page(request, market_pk, user_pk):
    user_id = get_object_or_404(User, pk=user_pk)
    market_id = get_object_or_404(Market, pk=market_pk)
    time = datetime.now()

    contact_detail = ContactDetail(
        user_id=user_id,
        market_id=market_id,
        time=time,
    )
    print(contact_detail)

    # options = QRCodeOptions(size='t', border=6, error_correction='L')

    year = str(time.year)
    month = str(time.month)
    day = str(time.day)
    hour = str(time.hour)
    time_str = year+month+day+hour

    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(contact_detail, image_factory=factory)
    # img.save(f'market/images/{user_id}{market_id}{time_str}.svg')
    drawing = svg2rlg(f"market/images/{user_id}{market_id}{time_str}.svg")
    dd=renderPM.drawToFile(drawing, f"market/images/{user_id}{market_id}{time_str}.png", fmt="PNG")
    
    return HttpResponse(dd, content_type="image/png")


def go(request):
    url = "http://127.0.0.1:8000/market/qrcode_page/1/1"
    response = requests.get(url=url)
    print('response.text')
    print(response.text)
    # print(response.data)
    # print(response.data)
    # print(response.data)
    # print(response.data)
    return response



    # print(time_str)
    
    # response = FileResponse(open(f'market/images/{user_id}.jpg', 'rb'))
    
    # context = dict(
    #     response=contact_detail
    # )

    # return redirect('market:send_file',  market_pk, user_pk)
    # return render(request, 'market/qrcode_page.html', context=context)


def send_file(response, market_pk, user_pk):
    market_id = get_object_or_404(Market, pk=market_pk)
    user_id = get_object_or_404(User, pk=user_pk)

    time = datetime.now()
    year = str(time.year)
    month = str(time.month)
    day = str(time.day)
    hour = str(time.hour)
    time_str = year+month+day+hour
    img = open(f'market/images/{user_id}{market_id}{time_str}.svg', 'rb')
    response = FileResponse(img)
    return response
 