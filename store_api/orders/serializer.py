from rest_framework import serializers
from . import models


class OrderItemsSerializer(serializers.ModelSerializer):  

  class Meta:
    model = models.OrderItems
    fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
  #The name order is the related_name in the foreign key for order_items

  order_items = OrderItemsSerializer(many=True, read_only=True)
  

class OrdersSerializer(serializers.ModelSerializer):

  order_items = OrderItemsSerializer(many=True, read_only=True) 

  class Meta:
    model = models.Orders
    fields = '__all__'

