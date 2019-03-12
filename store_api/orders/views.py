from . import models, serializer
from rest_framework import viewsets

class OrdersViewSet(viewsets.ModelViewSet):
  queryset = models.Orders.objects.all()
  serializer_class = serializer.OrdersSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):
  queryset = models.OrderItems.objects.all()
  serializer_class = serializer.OrderItemsSerializer