from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import renderers
from .models import Satellite
from .serializers import SatelliteSerializer

class SatelliteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    renderer_classes = [renderers.JSONRenderer]

    queryset = Satellite.objects.all()
    serializer_class = SatelliteSerializer
