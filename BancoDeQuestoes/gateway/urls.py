from django.urls import include, re_path, path
from .views import *
from rest_framework import routers
from . import views

app_name = 'gateway'

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet, basename='Post')
router.register(r'albun', views.AlbumViewSet, basename='Album')
router.register(r'api', views.APIViewSet, basename='API')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]