from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def create(self, request):
        user = request.user
        if user.is_staff == True:
            data = request.data
            instance = User.objects.create(**data)
            serializer = UserSerializer(instance, context = {'request':request}, many = False)
            return Response(serializer.data)
        else:
            return JsonResponse({'error': "You don't have permission to perform this action."})





    def update(self, request, pk=None, *args, **kwargs):
        user = request.user
        if user.is_staff == True:        
            instance = self.get_object()

            serializer = self.serializer_class(instance, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()
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