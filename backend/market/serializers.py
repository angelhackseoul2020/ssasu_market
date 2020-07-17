from rest_framework import serializers
from .models import Market

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class VisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitor
        fields = ['id', 'user_id']

    def create(self, validated_data):      
        visitor = Visitor(
                user_id=validated_data['user_id']
            )
        visitor.save()
        return visitor