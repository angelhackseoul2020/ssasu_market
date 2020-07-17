from django.shortcuts import render, redirect, get_object_or_404
from .models import VisitoRecord, Market, Review, Openhour, Visitor
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from datetime import datetime
from .serializers import MarketSerializer, VisitorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from qr_code.qrcode.utils import ContactDetail, QRCodeOptions


# market 관련 api
@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)


# visitor 정보 저장 api
@api_view(['POST'])
@permission_classes([AllowAny])
def makevisitor(request):
    serializer = VisitorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return HttpResponse('Sucess Visitor')


# qrcode 보여주는 api
DEMO_CONTACT = ContactDetail(
        name='gyyoon4u',
        market='tong-in market',
    )
DEMO_OPTIONS = QRCodeOptions(size='t', border=6, error_correction='L')

def qrcode_page(request):
    visitor = Visitor.objects.only()
    context = dict(
        contact_detail=DEMO_CONTACT,
        options_example=DEMO_OPTIONS,
        visitor=visitor['user_id']
    )

    # Render the index page.
    return render(request, 'market/qrcode_page.html', context=context)
