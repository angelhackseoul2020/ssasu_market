from rest_framework import serializers
from .models import Market, Review, Item, Store

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','market','title','content','score','image','date', 'user_id']

class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title','content','score','image']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class StoreUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'phone', 'image', 'address', 'open_hour', 'close_hour', 'content']

class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['price', 'content', 'name', 'image']
