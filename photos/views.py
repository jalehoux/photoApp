from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Photo
from django.conf import settings 
from .serializer import PhotoSerializer


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer