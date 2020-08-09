from rest_framework import serializers
from . import models

class ClientsCategorySerializer(serializers.ModelSerializer):  

  class Meta:
    model = models.Clients_category
    fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.Clients
    fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.About
    fields = '__all__'