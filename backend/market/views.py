from django.shortcuts import render, redirect, get_object_or_404
from .models import VisitoRecord, Market, Review, Openhour
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from datetime import datetime
from .serializers import MarketSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User 

# market 관련 api
@api_view(['GET'])
@permission_classes([AllowAny])
def info(request):
    markets = Market.objects.all()
    serializer = MarketSerializer(markets, many=True)
    return Response(serializer.data)

# 리뷰 하나 쓰기
# @permission_classes([IsAuthenticated])
@api_view(['POST'])
@permission_classes([AllowAny])
def write_review(request):
    user = request.data.get('user')
    market = request.data.get('market')
    title = request.data.get('title')
    content = request.data.get('content')
    score = request.data.get('score')
    image = request.data.get('image')
    review = Review()
    user =  get_object_or_404(User, pk=user) 
    review.user = user
    review.market = market
    review.title = title
    review.score = score
    review.image = image
    review.content = content
    review.save()
    serializer = ReviewSerializer(instance=review)
    return Response(serializer.data)

