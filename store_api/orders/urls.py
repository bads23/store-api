from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'orders'

router = DefaultRouter()

router.register('list', views.OrdersViewSet, 'orders')
router.register('orderItems', views.OrderItemsViewSet, 'orderItems')
router.register('postas', views.PostasViewSet, 'postas')
router.register('status', views.OrderStatusViewSet, 'status')
router.register('stats', views.OrderStats, 'stats')
router.register('itemssold', views.ItemsSoldViews, 'itemssold')

urlpatterns = router.urls