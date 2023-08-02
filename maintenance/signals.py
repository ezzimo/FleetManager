from django.db.models.signals import post_save
from django.dispatch import receiver
from maintenance.models import MaintenanceRecord


@receiver(post_save, sender=MaintenanceRecord)
def update_inventory(sender, instance, **kwargs):
    for part in instance.parts_used.all():
        part.quantity -= 1
        part.save()
