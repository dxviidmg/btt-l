from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404


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
    visits = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.id

    def get_visits(self, obj):
        return Visit.objects.filter(product=obj).count()

    class Meta:
        model = Product
        fields = ("url", "brand", "name", "sku", "price", "visits")