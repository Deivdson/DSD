from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Album

class SerializadorAluno(serializers.ModelSerializer):
    class Meta:
        fields = ('albumId', 'id', 'title', 'url', 'thumbnailUrl')

class SerializadorCronograma(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'privacidade', 'titulo', 'aluno')

class SerializadorTarefa(serializers.ModelSerializer): 
    class Meta: 
        fields = ('id', 'titulo', 'assunto', 'descricao', 'hora_inicio', 'data', 'status', 'cronograma')

class SerializadorAlbum(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('albumId', 'id', 'title', 'url', 'thumbnailUrl')