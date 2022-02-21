from django.conf import settings 

from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['name','author','description', 'image', 'created']
