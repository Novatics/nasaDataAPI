from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SatelliteViewSet
from django.conf.urls import include

router = DefaultRouter()
router.register(r'satellites', SatelliteViewSet, basename='sattelite')
urlpatterns = router.urls
