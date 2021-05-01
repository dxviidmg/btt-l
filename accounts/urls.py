from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
]



#from rest_framework import routers
#from . import views
#from django.urls import path, include