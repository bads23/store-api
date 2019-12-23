from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'users'

router = DefaultRouter()
router.register('usersList', views.CustomUserViewSet, 'users list')
router.register('userDetails', views.UserDetailsViewSet, 'user details')
router.register('visitors', views.VisitorsViewSet, 'visitors')
router.register('visitorStats', views.VisitorStatsViewSet, 'visitorStats')

urlpatterns = router.urls
