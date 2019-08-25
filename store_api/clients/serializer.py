from rest_framework import serializers
from . import models

class ClientsCategorySerializer(serializers.ModelSerializer):  

  class Meta:
    model = models.Clients_category
    fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
  category = serializers.SlugRelatedField(read_only=True, slug_field='category')

  class Meta:
    model = models.Clients
    fields = '__all__'
