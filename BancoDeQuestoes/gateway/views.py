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
from rest_framework import mixins, generics, permissions

class APIViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = SerializadorAPI
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(res.status_code)
    response = json.loads(res.text)   
    queryset = response
    serializer_class = SerializadorPost
    permission_classes = [permissions.AllowAny]

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
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        pass