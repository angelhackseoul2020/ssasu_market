from rest_framework import serializers
from .models import User
from django.core.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'userid']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userid', 'password', 'phone']
            
    def create(self, validated_data):
        user = User(
            userid=validated_data['userid'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password', 'changepassword']
