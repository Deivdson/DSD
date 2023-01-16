from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class SerializadorAlbum(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('albumId', 'id', 'title', 'url', 'thumbnailUrl')

class SerializadorAPI(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = ('title', 'url')

class SerializadorPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('userId', 'id', 'title', 'body')