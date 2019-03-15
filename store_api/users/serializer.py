from rest_framework import serializers
from . import models

class CustomUserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.CustomUser
    fields = '__all__'

class UserDetailsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.UserDetails
    fields = '__all__'    