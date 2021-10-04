from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import FuelConsumption, GazStation, Refuel


# Register your models here.
@admin.register(GazStation)
class GazStationAdmin(OSMGeoAdmin):
    list_display = ("name", "Controlor_id", "city_id", "geo_localization", "created_at", "updated_at", "is_active")


admin.site.register(Refuel)
admin.site.register(FuelConsumption)
