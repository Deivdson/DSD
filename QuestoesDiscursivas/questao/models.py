from django.db import models

# Create your models here.
class Lista(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=60)

    def __str__(self):
        return self.titulo + " - " + self.id

class Questao(models.Model):
    titulo = models.CharField(max_length=20)
    pergunta = models.CharField(max_length=60)
    resposta = models.CharField(max_length=60)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " - " + self.id

