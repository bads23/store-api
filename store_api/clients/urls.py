from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'clients'

router = DefaultRouter()

router.register('clients', views.ClientsViewSet, 'clients')
router.register('clientsCategory', views.ClientsCategoryViewSet, 'clientsCategory')

urlpatterns = router.urls