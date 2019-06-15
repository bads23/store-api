from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):  

  class Meta:
    model = models.News
    fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Events
    fields = '__all__'