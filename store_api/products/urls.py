from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'products'

router = DefaultRouter()

router.register(
  ''sudo su - postgres
, views.ProductsViewSet, 'products')

urlpatterns = router.urls