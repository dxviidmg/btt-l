from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response


class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = ("url", "name")


#class VisitsSerializer(serializers.HyperlinkedModelSerializer):

#    class Meta:
#        model = Visits
#        fields = ('id', "url", "product", "user", "number", )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.id

    class Meta:
        model = Product
        fields = ("url", "brand", "name", "sku", "price")