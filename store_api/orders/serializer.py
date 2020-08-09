from rest_framework import serializers
from . import models


class OrderItemsSerializer(serializers.ModelSerializer):
  def __init__(self, *args, **kwargs):
    many = kwargs.pop('many', True)
    super(OrderItemsSerializer, self).__init__(many=many, *args, **kwargs)

  name = serializers.CharField(source='product.name', read_only=True)
  price = serializers.IntegerField(source='product.price', read_only=True)


  class Meta:
    model = models.OrderItems
    fields ='__all__'


class OrdersSerializer(serializers.ModelSerializer):
  #The name order is the related_name in the foreign key for order_items
  order_items = OrderItemsSerializer(many=True, read_only=True) 
  user_email = serializers.CharField(source='user.email', read_only=True)
  user_fname = serializers.CharField(source='user.first_name', read_only=True)
  user_lname = serializers.CharField(source='user.last_name', read_only=True)
  posta = serializers.CharField(source='delivery.name', read_only=True)
  # payment_mode = serializers.CharField(source='payment_mode', read_only=True)
  pay_status = serializers.CharField(source='status', read_only=True)
  status_name = serializers.CharField(source='status.name', read_only=True)
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