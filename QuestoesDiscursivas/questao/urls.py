from django.urls import include, re_path, path
from .views import *
from rest_framework import routers
from . import views

app_name = 'questao'

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'lista', views.ListaViewSet, basename='Lista')
router.register(r'pergunta', views.QuestaoViewSet, basename='Pergunta')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]