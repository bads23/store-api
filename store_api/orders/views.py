from . import models, serializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .helpers import GatherStats, ItemsSold
from rest_framework import mixins
from .mailor import send_order_email, send_confirm_email


class ItemsSoldViews(viewsets.ViewSet):
    def list(self, request):
        return Response(ItemsSold())


class OrderStats(viewsets.ViewSet):
    def list(self, request):
        return Response(GatherStats(request))


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = models.Orders.objects.all()
    serializer_class = serializer.OrdersSerializer
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('user', 'status', )
    order_fields = ("date_added",)


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializer.OrderItemsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostasViewSet(viewsets.ModelViewSet):
    queryset = models.Postas.objects.all()
    serializer_class = serializer.PostasSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = models.OrderStatus.objects.all()
    serializer_class = serializer.OrderStatusSerializer


class SendEmailView(viewsets.ViewSet):

    def create(self, request):
        data = {}
        print(request.data)
        if(send_order_email(request.data) != False):
            send_confirm_email(request.data)
            data['message'] = 'Message sent!'
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['message'] = 'Message Not Sent! Try again later.'
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
