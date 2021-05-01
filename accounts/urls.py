from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [

    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]