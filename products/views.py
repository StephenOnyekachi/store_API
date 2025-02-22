
from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductsSerializers
from .models import Products

# Create your views here.

class ProductsList(generics.ListCreateAPIView):
    serializer_class = ProductsSerializers

    def get_queryset(self):
        queryset = Products.objects.all()
        product = self.request.query_params.get(queryset)
        if product is not None:
            queryset = queryset.filter(product=product)
        return queryset

class ProductInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializers
    queryset = Products.objects.all()