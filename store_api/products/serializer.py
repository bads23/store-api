from rest_framework import serializers
from .models import Catalog, Categories, Inventory, Images

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('stock',)

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images 
        fields = ('id', 'catalog', 'path', 'is_avatar')

class CatalogSerializer(serializers.ModelSerializer):
    stock = serializers.SlugRelatedField(read_only=True, slug_field='stock')
    images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ('name', 'price', 'description', 'category', 'stock', 'images')


class CategoriesSerializer(serializers.ModelSerializer):
    '''
      #NOTE: The name items is the related_name in the foreign key for category in catalog. 
      # related_names has to be there for it to work.
    '''

    items = CatalogSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ('id', 'name', 'items')

