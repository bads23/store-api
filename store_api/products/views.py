import os
import uuid

from django.conf import settings

from . import models
from . import serializer
from rest_framework import viewsets, parsers
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = models.Catalog.objects.all()
    serializer_class = serializer.CatalogSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('category', 'subcategory', 'productclass',)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializer.CategoriesSerializer


class SubcategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Subcategories.objects.all()
    serializer_class = serializer.SubcategoriesSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('category',)


class ProductclassViewSet(viewsets.ModelViewSet):
    queryset = models.Productclass.objects.all()
    serializer_class = serializer.ProductclassSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('subcategory',)


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = models.Inventory.objects.all()
    serializer_class = serializer.InventorySerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = models.Images.objects.all()
    serializer_class = serializer.ImagesSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, )

    @action(detail=True)
    def upload(self, request, serializer):
        serializer.save(catalog=request.catalog, path=request.data.get(
            'file'), is_avatar=request.is_avatar)
