from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly 
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Sucess Create ID')

@api_view(['GET'])
@permission_classes([AllowAny])
def myinfo(request, userid):
    user = get_object_or_404(User, userid=userid)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data)

@api_view(['PUT','DELETE'])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def editinfo(request, user_id):
    user = authenticate(request, userid=userid, password=password)
    if user is not None:
        if request.method == "PUT":
            serializer = UserUpdateSerializer(
                data = request.data, instance = user
            )
            serializer.save()
            return Response(True)
        else:  # DELETE
            user.delete()
            return Response("message: deleted")
    else: return Response("Password Matching Error")
