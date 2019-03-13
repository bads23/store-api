from rest_framework import viewsets
from .models import PaymentModes, Payments
from .serializer import PaymentModesSerializer, PaymentsSerializer

class PaymentModesViewSet(viewsets.ModelViewSet):
  
  queryset=PaymentModes.objects.all()
  serializer_class=PaymentModesSerializer


class PaymentViewSet(viewsets.ModelViewSet):
  
  queryset=Payments.objects.all()
  serializer_class=PaymentsSerializer