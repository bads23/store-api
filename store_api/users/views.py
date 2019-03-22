from . import models
from . import serializer
from rest_framework import viewsets

class CustomUserViewSet(viewsets.ModelViewSet):
  queryset = models.CustomUser.objects.all()
  serializer_class = serializer.CustomUserSerializer

class UserDetailsViewSet(viewsets.ModelViewSet):
  queryset = models.UserDetails.objects.all()
  serializer_class = serializer.UserDetailsSerializer
