from rest_framework import serializers
from .models import SalesCheck, Product, Line


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'description', 'stock', 'available')


class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'value', 'available')


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ( 'product', 'value', 'cuantity')


class SalesCheckSerializer(serializers.ModelSerializer):
    lines  = LineSerializer(many = True)
    class Meta:
        model = SalesCheck
        fields = ('totalToPay', 'date', 'lines')

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        sales_check = SalesCheck.objects.create(**validated_data)
        for line_data in lines_data:
            Line.objects.create(salesCheck=sales_check, **line_data)
        return sales_check
