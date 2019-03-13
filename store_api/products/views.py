from .models import Catalog, Categories, Inventory
from .serializer import CatalogSerializer, CategoriesSerializer, InventorySerializer
from rest_framework import viewsets

class CatalogViewSet(viewsets.ModelViewSet):
  queryset = Catalog.objects.all()
  serializer_class = CatalogSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Categories.objects.all()
  serializer_class = CategoriesSerializer

class InventoryViewSet(viewsets.ModelViewSet):
  queryset = Inventory.objects.all()
  serializer_class = InventorySerializer