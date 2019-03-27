from rest_framework import serializers
from .models import Catalog, Categories, Inventory, Images


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ('name', 'price', 'description', 'category')


class CategoriesSerializer(serializers.ModelSerializer):
    '''
      #NOTE: The name items is the related_name in the foreign key for category in catalog. 
      # related_names has to be there for it to work.
    '''

    items = CatalogSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ('id', 'name', 'items')


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('id', 'stock', 'product')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'name', 'image')
