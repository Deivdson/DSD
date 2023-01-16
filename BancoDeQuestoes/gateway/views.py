from django.shortcuts import render
from rest_framework import status, viewsets
import requests, json
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response

class DailyViewSet(viewsets.ModelViewSet):
    #res = requests.get('https://localhost:8000/api/')
    #print(res.status_code)
    #response = json.loads(res.text)   
    #queryset = response
    #serializer_class = SerializadorDaily
    pass

class PostViewSet(viewsets.ModelViewSet):
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(res.status_code)
    response = json.loads(res.text)   
    queryset = response
    serializer_class = SerializadorPost

    def create(self, request, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/posts'        
        json_data = json.loads(str(request.body, encoding='utf-8'))
        x = requests.post(url, json = json_data)
        print(x.text)
        print(request)
        entrada_serializer = self.get_serializer(data=request.data)
        headers = self.get_success_headers(entrada_serializer.data)
        pass
        return Response(status=status.HTTP_201_CREATED)

class AlbumViewSet(viewsets.ModelViewSet): 
    res = requests.get('https://jsonplaceholder.typicode.com/albums/1/photos')
    print(res.status_code)
    response = json.loads(res.text)   
    queryset = response
    serializer_class = SerializadorAlbum

    def create(self, request, *args, **kwargs):
        pass

class CronogramaViewSet(viewsets.ModelViewSet):
    #res = requests.get('https://localhost:8000/api/cronogramas/')
    #print(res.status_code)
    #response = json.loads(res.text)
    #queryset = response
    #serializer_class = SerializadorCronograma
#
    #def create(self, request, *args, **kwargs):
    #    return super().create(request, *args, **kwargs)
    pass

class TarefaViewSet(viewsets.ModelViewSet):
    #queryset = Tarefa.objects.all()
    #serializer_class = SerializadorTarefa
    pass

class AlunoViewSet(viewsets.ModelViewSet):
    #queryset = Aluno.objects.all()
    #serializer_class = SerializadorAluno
    pass