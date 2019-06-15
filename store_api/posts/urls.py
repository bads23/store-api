from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from . import views

app_name = 'posts'

router = DefaultRouter()

router.register('news', views.NewsViewSet, 'news')
router.register('events', views.EventsViewSet, 'events')

urlpatterns = router.urls