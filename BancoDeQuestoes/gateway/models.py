from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=500)

class Album(models.Model):
    albumId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    thumbnailUrl = models.CharField(max_length=50)

class Dailyschedule(models.Model):
    cronogramas = models.CharField(max_length=30)
    tarefas = models.CharField(max_length=30)
    alunos = models.CharField(max_length=30)


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario

class Cronograma(models.Model):
    privacidade = models.BooleanField(default = False)
    titulo = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='criado por',
        null=True
    )

    def __str__(self):
        return ("{0} - {1}").format(self.titulo, self.aluno)

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    assunto = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=100)
    hora_inicio = models.TimeField(default=timezone.now)
    data = models.DateTimeField('Data Cronograma')
    status = models.BooleanField(default=False)
    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao



