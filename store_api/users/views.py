from . import models
from . import serializer
from rest_framework import viewsets, status
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializer.CustomUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.UserDetails.objects.all()
    serializer_class = serializer.UserDetailsSerializer
