from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from .models import Station

# View to get the 6 nearest snotel station locations

# Define user location
# Hard coded to Boise ID for now, will add dynamic location input later
longitude = -116.208710
latitude = 43.603600

user_location = Point(longitude, latitude, srid=4326)

# Add view class for nearby Snotel stations
class Home(generic.ListView):
    model = Station
    context_object_name = 'stations'
    queryset = Station.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'stations/index.html'

