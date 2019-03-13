from rest_framework import serializers
from . import models

class OrdersSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Orders
    fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.OrderItems
    fields = '__all__'