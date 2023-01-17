from rest_framework import serializers
from .models import *

class SerializadorLista(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ('titulo', 'descricao')

class SerializadorQuestao(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = ('titulo', 'pergunta', 'lista')

class SerializadorAlternativa(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ('texto', 'correta', 'questao')