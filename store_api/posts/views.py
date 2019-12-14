from django.shortcuts import render
from . import models, serializer
from rest_framework import viewsets

class NewsViewSet(viewsets.ModelViewSet):
  queryset = models.News.objects.all()
  serializer_class = serializer.NewsSerializer

class EventsViewSet(viewsets.ModelViewSet):
  queryset = models.Events.objects.all()
  serializer_class = serializer.EventsSerializer


class EventsviewsViewSet(viewsets.ModelViewSet):
  queryset = models.EventsViews.objects.all()
  serializer_class = serializer.EventsviewsSerializer


class PostviewsViewSet(viewsets.ModelViewSet):
  queryset = models.PostViews.objects.all()
  serializer_class = serializer.PostviewsSerializer