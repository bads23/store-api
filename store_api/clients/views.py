from . import models, serializer
from rest_framework import viewsets

class ClientsViewSet(viewsets.ModelViewSet):
  queryset = models.Clients.objects.all()
  serializer_class = serializer.ClientsSerializer

class ClientsCategoryViewSet(viewsets.ModelViewSet):
  queryset = models.Clients_category.objects.all()
  serializer_class = serializer.ClientsCategorySerializer
