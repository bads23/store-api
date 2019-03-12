from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'users'

router = DefaultRouter()

router.register('users', views.CustomUserViewSet)
users_urlpatterns = router.urls

urlpatterns = [
  path('', views.CustomUserViewSet, 'users')
]