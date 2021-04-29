from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from .serializers import *

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer