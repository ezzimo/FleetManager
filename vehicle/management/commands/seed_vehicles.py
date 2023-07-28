# vehicle/management/commands/seed_vehicles.py
from django.core.management.base import BaseCommand
from vehicle.models import Make, VehicleModel, Vehicle
import random

class Command(BaseCommand):
    help = 'Seeds the database with vehicle data'

    def handle(self, *args, **options):
        # Delete all existing data
        Make.objects.all().delete()
        VehicleModel.objects.all().delete()
        Vehicle.objects.all().delete()

        # Create Makes
        makes = ['Ford', 'Mercedes-Benz', 'Toyota', 'Volkswagen', 'Chevrolet']
        make_objects = [Make.objects.create(name=make) for make in makes]

        # Create VehicleModels
        models = ['Transit', 'Sprinter', 'HiAce', 'Crafter', 'Express']
        model_objects = [VehicleModel.objects.create(name=model, place_number=random.randint(6, 16), make=make_objects[i]) for i, model in enumerate(models)]

        # Create Vehicles
        for i in range(25):
            Vehicle.objects.create(
                serie=f'Serie {i+1}',
                model=random.choice(model_objects)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded vehicle data'))
