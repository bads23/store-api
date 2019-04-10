from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PaymentModes, Payments
from .serializer import PaymentModesSerializer, PaymentsSerializer
from store_api.payments.at.mobile_checkout import pay


class PaymentModesViewSet(viewsets.ModelViewSet):

    queryset = PaymentModes.objects.all()
    serializer_class = PaymentModesSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        pay_request = pay(data)

        if(pay_request):
            pay_request['payment_mode'] = data['payment_mode']
            pay_request['amount'] = data['amount']
            pay_request['phone_number'] = data['phone_number']
            pay_request['name'] = 'test'

            serializer = self.get_serializer(data=pay_request)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
