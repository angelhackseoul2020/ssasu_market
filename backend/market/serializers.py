from rest_framework import serializers
from .models import Market, Review

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['market','title','content','score','image','date', 'user_id']