from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'payments'

router=DefaultRouter()
router.register('payments', views.PaymentViewSet, 'payments')
router.register('payment_modes', views.PaymentModesViewSet, 'payment_modes')
router.register('payment_notifications', views.PaymentNotificationsViewSet, 'payment_noti')

urlpatterns = router.urls