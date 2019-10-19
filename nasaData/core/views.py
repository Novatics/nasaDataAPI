from django.shortcuts import render

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
        queryset = Satellite.objects.all()
        satellite = get_object_or_404(queryset, pk=pk)
        serializer = SatelliteSerializer(user)
        return Response(serializer.data)
