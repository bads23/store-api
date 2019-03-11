from rest_framework import serializers
from .models import PaymentModes, Payments

class PaymentsSerializer(serializers.ModelSerializer):

  class Meta:
    model=Payments
    fields='__all__'

class PaymentModesSerializer(serializers.ModelSerializer):

  class Meta:
    model=PaymentModes
    fields='__all__'