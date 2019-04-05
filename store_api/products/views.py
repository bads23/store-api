import os
import uuid

from django.conf import settings

from .models import Catalog, Categories, Inventory, Images
from .serializer import CatalogSerializer, CategoriesSerializer, InventorySerializer, ImagesSerializer
from rest_framework import viewsets, parsers
from rest_framework.decorators import action


class CatalogViewSet(viewsets.ModelViewSet):
  '''Get all items in the catalog'''
  queryset = Catalog.objects.all()
  serializer_class = CatalogSerializer
  
  


class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Categories.objects.all()
  serializer_class = CategoriesSerializer

class InventoryViewSet(viewsets.ModelViewSet):
  queryset = Inventory.objects.all()
  serializer_class = InventorySerializer

class ImagesViewSet(viewsets.ModelViewSet):
  queryset = Images.objects.all()
  serializer_class = ImagesSerializer
  parser_classes = (parsers.FormParser, parsers.MultiPartParser)

  @action(detail=True)
  def upload(self, request, serializer):
    serializer.save(catalog=request.catalog, path=request.data.get('file'), is_avatar=request.is_avatar)
