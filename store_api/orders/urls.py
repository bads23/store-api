from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'orders'

router = DefaultRouter()

router.register(
  ''sudo su - postgres
, views.OrdersViewSet, 'orders')

urlpatterns = router.urls