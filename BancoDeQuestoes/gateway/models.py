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

class API(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)