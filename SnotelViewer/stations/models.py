from django.contrib.gis.db import models

# Create your models here.

class Station(models.Model):
    triple_id = models.CharField(max_length=12)
    station_name = models.CharField(max_length=200)
    station_id = models.CharField(max_length=10)
    state_code = models.CharField(max_length=2)
    state_name = models.CharField(max_length=100)
    network_code = models.CharField(max_length=20)
    network_name = models.CharField(max_length=50)
    elevation = models.IntegerField()
    location = models.PointField()
    county_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()