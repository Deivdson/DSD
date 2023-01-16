from django.db import models

# Create your models here.

class Album(models.Model):
    albumId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    thumbnailUrl = models.CharField(max_length=50)

    pass

