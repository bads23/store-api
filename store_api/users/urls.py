from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'users'

router = DefaultRouter()

<<<<<<< HEAD
router.register('users', views.CustomUserViewSet)
users_urlpatterns = router.urls
=======
router.register('', views.CustomUserViewSet, 'users')
>>>>>>> eb5c94505d15d01ad88708ff89a0a1700616de8b

urlpatterns = [
  path('', views.CustomUserViewSet, 'users')
]