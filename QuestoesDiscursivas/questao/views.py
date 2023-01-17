from django.shortcuts import render
from rest_framework import status, viewsets
from .models import *
from .serializers import *

# Create your views here.
class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = SerializadorLista

class QuestaoViewSet(viewsets.ModelViewSet):
    queryset = Questao.objects.all()
    serializer_class = SerializadorQuestao
