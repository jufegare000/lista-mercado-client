from rest_framework import serializers
from .models import SalesCheck, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'descriptions', 'stock', 'available')


class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'available')
