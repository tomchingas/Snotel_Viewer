from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin
from .models import Station

# Register your models here.

@admin.register(Station)
class stationsAdmin(OSMGeoAdmin):
    list_display = ('triple_id', 'station_name', 'location')
