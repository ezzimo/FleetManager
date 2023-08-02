from django.contrib import admin
from .models import MaintenanceType, MaintenanceRecord, MaintenanceSchedule

admin.site.register(MaintenanceType)
admin.site.register(MaintenanceRecord)
admin.site.register(MaintenanceSchedule)
