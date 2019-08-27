from rest_framework import serializers
# from .models import Catalog, Categories, Inventory, Images
from . import models


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Inventory
        fields = ('stock',)


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Images
        fields = ('id', 'catalog', 'path', 'is_avatar')


class CatalogSerializer(serializers.ModelSerializer):
    stock = serializers.SlugRelatedField(read_only=True, slug_field='stock')
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = models.Catalog
        fields = ('id', 'name', 'price', 'description', 'weight',
                  'category', 'subcategory', 'productclass', 'stock', 'images')


class ProductclassSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Productclass
        fields = '__all__'


class SubcategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subcategories
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    '''
      #NOTE: The name items is the related_name in the foreign key for category in catalog. 
      # related_names has to be there for it to work.
    '''

    items = CatalogSerializer(many=True, read_only=True)

    class Meta:
        model = models.Categories
        fields = ('id', 'name', 'items')
