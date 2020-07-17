from rest_framework import serializers
from .models import Market, VisitoRecord

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitoRecord
        fields = '__all__'
