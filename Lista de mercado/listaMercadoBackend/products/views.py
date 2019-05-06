from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import ProductMiniSerializer, ProductSerializer, SalesCheckSerializer
from .models import Product, SalesCheck


# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductMiniSerializer(products, many=True)
        return Response(serializer.data)


class SalesCheckView(viewsets.ModelViewSet):
    queryset = SalesCheck.objects.all()
    serializer_class = SalesCheckSerializer
