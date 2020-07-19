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
from django.contrib.auth.hashers import check_password




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

@api_view(['POST','DELETE'])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def editinfo(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        current_password = request.data.get("origin_password")
        if check_password(current_password, user.password): # 비밀번호 체크하기
            new_password = request.data.get("password1")
            password_confirm = request.data.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                return Response("message: password changed")
            else: return Response("error: 새로운 비밀번호를 다시 확인해주세요.")
        else: return Response("error: 현재 비밀번호가 일치하지 않습니다.")
    else:  # DELETE
        user.delete()
        return Response("message: deleted")

