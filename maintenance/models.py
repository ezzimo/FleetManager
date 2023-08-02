from django.db import models
from django.utils import timezone
from vehicle.models import Vehicle
from inventory.models import SparePart, Order
from inventory.constants import THRESHOLD, ORDER_QUANTITY
from django.utils.translation import gettext_lazy as _


class MaintenanceType(models.Model):
    class MaintenanceTypes(models.TextChoices):
        OIL_CHANGE = 'oil_change', _('Oil Change')
        TIRE_ROTATION = 'tire_rotation', _('Tire Rotation')
        BRAKE_INSPECTION = 'brake_inspection', _('Brake Inspection')
        FLUID_CHECKS = 'fluid_checks', _('Fluid Checks')
        AIR_FILTER_REPLACEMENT = 'air_filter_replacement', _('Air Filter Replacement')
        SPARK_PLUG_REPLACEMENT = 'spark_plug_replacement', _('Spark Plug Replacement')
        BATTERY_CHECK = 'battery_check', _('Battery Check')
        BELT_HOSE_INSPECTION = 'belt_hose_inspection', _('Belt and Hose Inspection')
        ALIGNMENT_CHECK = 'alignment_check', _('Alignment Check')
        EXHAUST_SYSTEM_INSPECTION = 'exhaust_system_inspection', _('Exhaust System Inspection')
        TRANSMISSION_SERVICE = 'transmission_service', _('Transmission Service')

    name = models.CharField(max_length=50, choices=MaintenanceTypes.choices)
    description = models.TextField()

    def __str__(self):
        return self.get_name_display()


class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    parts_used = models.ManyToManyField(SparePart, blank=True)

    def __str__(self):
        return f'{self.vehicle} {self.maintenance_type} on {self.date}'


class MaintenanceSchedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.SET_NULL, null=True)
    scheduled_date = models.DateField()
    notes = models.TextField(blank=True)
    parts_needed = models.ManyToManyField(SparePart, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for part in self.parts_needed.all():
            if part.quantity < THRESHOLD:
                Order.objects.create(spare_part=part, quantity=ORDER_QUANTITY)

    def __str__(self):
        return f'{self.vehicle} scheduled for {self.maintenance_type} on {self.scheduled_date}'