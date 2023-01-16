from django.urls import include, re_path, path
from .views import *
from rest_framework import routers
from . import views

app_name = 'gateway'

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'albuns', views.AlbumViewSet, basename='Album')
router.register(r'tarefas', views.TarefaViewSet, basename='Tarefa')
router.register(r'alunos', views.AlunoViewSet, basename='Aluno')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]