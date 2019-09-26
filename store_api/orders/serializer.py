from rest_framework import serializers
from . import models


class OrderItemsSerializer(serializers.ModelSerializer):  
  
  name = serializers.CharField(source='product.name', read_only=True)
  price = serializers.IntegerField(source='product.price', read_only=True)


  class Meta:
    model = models.OrderItems
    fields = ['order', 'quantity', 'name', 'price']
  

class OrdersSerializer(serializers.ModelSerializer):
  #The name order is the related_name in the foreign key for order_items
  order_items = OrderItemsSerializer(many=True, read_only=True) 

  class Meta:
    model = models.Orders
    fields = '__all__'


class PostasSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.Postas
    fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.OrderStatus
    fields = '__all__'