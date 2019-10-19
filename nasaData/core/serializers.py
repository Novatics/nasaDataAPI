from rest_framework import serializers
from .models import Satellite

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Satellite
		fields = ('id','satellite_type', 'name', 'description', 'launch_date')
