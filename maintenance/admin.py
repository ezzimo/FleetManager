from django.contrib import admin
from .models import MaintenanceType, Part, MaintenanceRecord, MaintenanceSchedule

admin.site.register(MaintenanceType)
admin.site.register(Part)
admin.site.register(MaintenanceRecord)
admin.site.register(MaintenanceSchedule)
