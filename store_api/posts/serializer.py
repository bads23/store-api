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

class EventsviewsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.EventsViews
    fields = '__all__'


class PostviewsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.PostViews
    fields = '__all__'