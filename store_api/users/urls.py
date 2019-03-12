from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'users'

router = DefaultRouter()

<<<<<<< HEAD
router.register(
  '', views.CustomUserViewSet, 'users')
=======
router.register('', views.CustomUserViewSet, 'users')
>>>>>>> 5b7bfaca0e4fe81c92edaf69cf5f476d23bc1fc0

urlpatterns = router.urls