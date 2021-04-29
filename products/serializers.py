from rest_framework import serializers
from .models import *

class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = ("url", "name")

class VisitsByProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = VisitsByProduct
        fields = ('id', "url", "product", "number")



class ProductSerializer(serializers.HyperlinkedModelSerializer):

#    visitas = VisitsByProductSerializer(many=False, read_only=True)
#    print(visitas)

    class Meta:
        model = Product
#        fields = ("url", "name", "sku", "price", "visitas")
        fields = ("url", "name", "sku", "price")
