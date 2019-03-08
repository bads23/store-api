from .models import Products
from .serializer import ProductsSerializer
from rest_framework import viewsets

class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer
