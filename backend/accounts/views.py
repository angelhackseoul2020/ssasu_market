from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly 
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Sucess Create ID')