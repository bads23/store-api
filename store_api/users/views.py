from .models import CustomUser
from .serializer import CustomUserSerializer
from rest_framework import viewsets

class CustomUserViewSet(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer
