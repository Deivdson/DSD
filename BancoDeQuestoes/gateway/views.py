from django.shortcuts import render
from rest_framework import status, viewsets
import requests, json
from .serializers import SerializadorAluno, SerializadorAlbum
# Create your views here.


class AlbumViewSet(viewsets.ModelViewSet): 
    res = requests.get('https://jsonplaceholder.typicode.com/albums/1/photos')
    print(res.status_code)
    response = json.loads(res.text)   
    queryset = response
    serializer_class = SerializadorAlbum
    def Post():
        pass

class TarefaViewSet(viewsets.ModelViewSet):
    #queryset = Tarefa.objects.all()
    #serializer_class = SerializadorTarefa
    pass

class AlunoViewSet(viewsets.ModelViewSet):
    #queryset = Aluno.objects.all()
    #serializer_class = SerializadorAluno
    pass