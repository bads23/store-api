from .models import Catalog, Categories, Inventory
from .serializer import CatalogSerializer, CategoriesSerializer, InventorySerializer, ImagesSerializer
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

class ImagesViewSet(viewsets.ModelViewSet):
    def post(self, request, format=None):
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)