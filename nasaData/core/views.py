from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Satellite
from .serializers import SatelliteSerializer

from .data_manager import load_data, get_satellite_coordinates


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


class CoondinatesViewSet(viewsets.ViewSet):

    renderer_classes = [renderers.JSONRenderer]

    def retrieve(self, request, pk=None):

        if(self.request.query_params.get('lon') == None
            or self.request.query_params.get('lat') == None
            or self.request.query_params.get('alt') == None ):
            print("NAO TEM TUDO")
            data = {
                'id':pk,
                'coordinates':None,
            }

        else:

            longitude = float(request.query_params.get('lon'))
            latitude = float(request.query_params.get('lat'))
            altitude = float(request.query_params.get('alt'))

            coordinates = get_satellite_coordinates(longitude, latitude, altitude, pk)
            print(coordinates)
            print(coordinates[0])
            data = {
                'id':pk,
                'coordinates':{
                    'azi':coordinates[0],
                    'alt':coordinates[1],
                },
            }

        return Response(data)
