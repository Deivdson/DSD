from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

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

class SerializadorDaily(serializers.ModelSerializer):
    class Meta:
        model = Dailyschedule
        fields = ('cronogramas', 'tarefas', 'alunos')

class SerializadorPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('userId', 'id', 'title', 'body')