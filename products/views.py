from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail


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
            instance = Product.objects.create(**data, brand=brand)
            serializer = ProductSerializer(instance, context = {'request':request}, many = False)
            return Response(serializer.data)
        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})

    def retrieve(self, request, pk=None):
        user = request.user
        instance = self.get_object()
        if user.is_staff == False:

            visits, visits_created = Visits.objects.get_or_create(user=user, product=instance)
            visits.number = visits.number + 1
            visits.save()

        serializer = ProductSerializer(instance, context = {'request':request}, many = False)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        user = request.user
        if user.is_staff == True:        
            instance = self.get_object()

            serializer = self.serializer_class(instance, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()

            msg = 'The product with sku ' + instance.sku + ' was updated.' + '\nThe attributes are:\n'
            attributes = list('*' + k for k in request.data.keys())
            attributes = '\n'.join(list(attributes))
            msg = msg + attributes

            admin_emails = list(User.objects.filter(is_staff=True).values_list('email', flat=True))
            send_mail('Product update', msg, None, admin_emails, fail_silently=False)
            return Response(serializer.data)

        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})

    def destroy(self, request, pk=None):
        user = request.user
        if user.is_staff == True:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})