from . import models
from . import serializer
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from .mailor import send_contact_form
from .helpers import VisitorStats

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

    @action(detail=False)
    def me(self, request):
        serialized = serializer.CustomUserSerializer(request.user)
        return Response(serialized.data)


class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.UserDetails.objects.all()
    serializer_class = serializer.UserDetailsSerializer

class VisitorsViewSet(viewsets.ModelViewSet):
    queryset = models.Visitors.objects.all()
    serializer_class = serializer.VisitorsSerializer

class VisitorStatsViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(VisitorStats())


class ContactFormViewSet(viewsets.ViewSet):

    def create(self, request):
        data = {}
        if(send_contact_form(request.data) == True):
            data['message'] = 'Message sent!'
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['message'] = 'Message Not Sent! Try again later.'
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)