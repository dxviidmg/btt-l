"""
from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()

router.register('brands', views.BrandViewSet)
router.register('products', views.ProductViewSet)

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [

    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),

    

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
"""