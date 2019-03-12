from rest_framework import serializers
from .models import Catalog, Categories, Inventory

class CatalogSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Catalog
    fields = ('name', 'price', 'description', 'category',)



class CategoriesSerializer(serializers.ModelSerializer):

  class Meta:
    model = Categories
    fields = ('id','name',)
   

class InventorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Inventory
    fields = ('id','stock', 'product',)