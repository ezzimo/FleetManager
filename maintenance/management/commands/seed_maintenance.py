from django.core.management.base import BaseCommand
from maintenance.models import MaintenanceType, Part, MaintenanceRecord, MaintenanceSchedule
from vehicle.models import Vehicle
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Seeds the database with Maintenance data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self._create_maintenance_data()
        self.stdout.write('Done.')

    def _create_maintenance_data(self):
        # Create MaintenanceTypes
        for type_choice in MaintenanceType.MaintenanceTypes.choices:
            MaintenanceType.objects.create(name=type_choice[0], description=f'Description for {type_choice[1]}')

        # Create Parts
        for i in range(1, 16):  # Changed to create 15 parts
            Part.objects.create(name=f'Part {i}', description=f'Description for Part {i}', count=random.randint(1, 100))

        # Get all vehicles
        vehicles = Vehicle.objects.all()

        # Get all maintenance types
        maintenance_types = MaintenanceType.objects.all()

        # Get all parts
        parts = Part.objects.all()

        # Create MaintenanceRecords and MaintenanceSchedules for each vehicle
        for vehicle in vehicles:
            for maintenance_type in maintenance_types:
                # Create 10 MaintenanceRecords for each vehicle and maintenance type
                for _ in range(10):
                    record = MaintenanceRecord.objects.create(
                        vehicle=vehicle,
                        maintenance_type=maintenance_type,
                        date=timezone.now(),
                        notes=f'Notes for {vehicle} {maintenance_type}',
                        cost=random.uniform(50, 500)
                    )
                    # Add random parts to the record
                    record.parts_used.add(*random.choices(parts, k=random.randint(1, len(parts))))

                # Create 5 MaintenanceSchedules for each vehicle and maintenance type
                for _ in range(5):
                    MaintenanceSchedule.objects.create(
                        vehicle=vehicle,
                        maintenance_type=maintenance_type,
                        scheduled_date=timezone.now() + timezone.timedelta(days=random.randint(1, 365)),
                        notes=f'Scheduled maintenance for {vehicle} {maintenance_type}'
                    )
