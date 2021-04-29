from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response

class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = ("url", "name")

class VisitsByProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = VisitsByProduct
        fields = ('id', "url", "product", "number")



class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ("url", "name", "sku", "price")

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request.user.is_staff == True: 
            return instance
        else:
            #Error
#            return Response({'message': 'Fecha promesa de pago actualizada de manera correcta'}, status=200)
            return Response('')


