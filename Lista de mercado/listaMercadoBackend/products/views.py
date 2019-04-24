from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import ProductMiniSerializer, ProductSerializer
from .models import Product, SalesCheck


# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        movies = ProductSerializer.objects.all()
        serializer = ProductMiniSerializer(movies, many=True)
        return Response(serializer.data)
