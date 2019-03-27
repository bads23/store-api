from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'products'

router = DefaultRouter()

router.register('catalog', views.CatalogViewSet, 'catalog')
router.register('categories', views.CategoriesViewSet, 'categories')
router.register('inventory', views.InventoryViewSet, 'inventory')
router.register('images', views.ImagesViewSet, 'images')


urlpatterns = router.urls