from . import models, serializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = models.Clients.objects.all()
    serializer_class = serializer.ClientsSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('category', )


class ClientsCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Clients_category.objects.all()
    serializer_class = serializer.ClientsCategorySerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = models.Music.objects.all()
    serializer_class = serializer.MusicSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('active', )


class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializer.AboutSerializer
