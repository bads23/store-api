from rest_framework import serializers
from . import models


class OrderItemsSerializer(serializers.ModelSerializer):  
  
  name = serializers.CharField(source='product.name', read_only=True)
  price = serializers.IntegerField(source='product.price', read_only=True)


  class Meta:
    model = models.OrderItems
    # fields = ['order', 'quantity', 'name', 'price']
    fields ='__all__'

class OrdersSerializer(serializers.ModelSerializer):
  #The name order is the related_name in the foreign key for order_items
  order_items = OrderItemsSerializer(many=True, read_only=True) 
  user_email = serializers.CharField(source='user.email', read_only=True)
  user_fname = serializers.CharField(source='user.first_name', read_only=True)
  user_lname = serializers.CharField(source='user.last_name', read_only=True)
  pickup = serializers.CharField(source='delivery.name', read_only=True)
  mode = serializers.CharField(source='payment_mode', read_only=True)
  pay_status = serializers.CharField(source='status', read_only=True)
  amount = serializers.IntegerField(source='payment.amount', read_only=True)
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