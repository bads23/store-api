from .models import Orders
from .serializer import OrdersSerializer
from rest_framework import viewsets

class OrdersViewSet(viewsets.ModelViewSet):
  queryset = Orders.objects.all()
  serializer_class = OrdersSerializer
