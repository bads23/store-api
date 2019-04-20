from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import PaymentModes, Payments, PaymentNotifications
from .serializer import PaymentModesSerializer, PaymentsSerializer, PaymentNotificationsSerializer
from store_api.payments.at.mobile_checkout import pay, generateOrderName
from store_api.payments.at.updatePayments import updatePayment
import json


class PaymentModesViewSet(viewsets.ModelViewSet):

    queryset = PaymentModes.objects.all()
    serializer_class = PaymentModesSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('kyc', 'status',)
    order_fields = ('id',)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['kyc'] = generateOrderName()
        pay_request = pay(data)

        if(pay_request):
            pay_request['payment_mode'] = data['payment_mode']
            pay_request['amount'] = data['amount']
            pay_request['phone_number'] = data['phone_number']
            pay_request['name'] = 'test'
            pay_request['kyc'] = data['kyc']

            serializer = self.get_serializer(data=pay_request)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentNotificationsViewSet(viewsets.ModelViewSet):

    queryset = PaymentNotifications.objects.all()
    serializer_class = PaymentNotificationsSerializer

    def create(self, request, *args, **kwargs):
        notification = request.data
        note = {}
        note['transaction_id'] = notification['transactionId']
        metadata = notification['metadata']
        note['kyc'] = metadata['kyc']
        note['status'] = notification['status']
        note['metadata'] = notification['description']
        updatePayment(note)

        serializer = self.get_serializer(data=note)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
