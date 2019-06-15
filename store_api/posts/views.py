from django.shortcuts import render
from . import models, serializer
from rest_framework import viewsets

class NewsViewSet(viewsets.ModelViewSet):
  queryset = models.News.objects.all()
  serializer_class = serializer.NewsSerializer

class EventsViewSet(viewsets.ModelViewSet):
  queryset = models.Events.objects.all()
  serializer_class = serializer.EventsSerializer