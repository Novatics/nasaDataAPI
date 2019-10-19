from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import SatelliteViewSet, CoondinatesViewSet
from django.conf.urls import include

router = DefaultRouter()
router.register(r'satellites', SatelliteViewSet, basename='sattelite')
router.register(r'coordinates', CoondinatesViewSet, basename='coordinate')

urlpatterns = router.urls
