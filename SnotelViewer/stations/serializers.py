from rest_framework import serializers
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('triple_id', 'station_name', 'station_id', 'state_code', 'state_name', 'network_code', 'network_name', 'elevation', 'location', 'county_name', 'start_date', 'end_date')