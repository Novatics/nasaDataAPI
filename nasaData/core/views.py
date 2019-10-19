from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response
from .models import Satellite
from .serializers import SatelliteSerializer

from .data_manager import load_data

class SatelliteViewSet(viewsets.ViewSet):

    """
    A simple ViewSet for listing or retrieving Satellites.
    """

    renderer_classes = [renderers.JSONRenderer]

    def list(self, request):
        load_data()
        queryset = Satellite.objects.all()
        serializer = SatelliteSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        load_data()
        satellite = get_object_or_404(Satellite, pk=pk)
        serializer = SatelliteSerializer(satellite)
        return Response(serializer.data)
