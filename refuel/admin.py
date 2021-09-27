from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis.geos import Point

from .forms import GazStationCreationForm
from .models import FuelConsumption, GazStation, Refuel

# Register your models here.
admin.site.register(GazStation)


admin.site.register(Refuel)
admin.site.register(FuelConsumption)
