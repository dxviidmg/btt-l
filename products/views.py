from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated 

class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all().order_by('id')
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    
    def create(self, request):
        user = request.user
        if user.is_staff == True:
            data = request.data
            brand_id = request.data.pop('brand')
            brand = Brand.objects.get(id=brand_id)
            product = Product.objects.create(**data, brand=brand)
            serializer = ProductSerializer(product, context = {'request':request}, many = False)
            return Response(serializer.data)
        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})

    def retrieve(self, request, pk=None):
        user = request.user
        product = Product.objects.get(id = pk)
        if user.is_staff == False:


            visits, visits_created = Visits.objects.get_or_create(user=user, product=product)
            visits.number = visits.number + 1
            visits.save()

        serializer = ProductSerializer(product, context = {'request':request}, many = False)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        user = request.user
        product = Product.objects.get(id = pk)
        if user.is_staff == True:
            print('Envio de correos')
        
            product = Product.objects.get(id = pk)
            serializer = ProductSerializer(product, context = {'request':request}, many = False)
            return Response(serializer.data)
        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})

    def destroy(self, request, pk=None, *args, **kwargs):
        print('entre')
        user = request.user
        if user.is_staff == True:
            print('Se va a borrar')
            return Response(serializer.data)
        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})



