from django.core.management.base import BaseCommand
from inventory.models import SparePart, Order
import random
import faker

class Command(BaseCommand):
    help = 'Seeds the database with SparePart and Order data'

    def handle(self, *args, **options):
        fake = faker.Faker()

        self.stdout.write('Deleting old data...')
        SparePart.objects.all().delete()
        Order.objects.all().delete()

        self.stdout.write('Creating new data...')
        for _ in range(100):  # Adjust the range as needed
            spare_part = SparePart.objects.create(
                name=fake.word(),
                description=fake.text(),
                quantity=random.randint(1, 100),
                minimum_quantity=random.randint(1, 50),
            )

            if spare_part.quantity < 10:  # Assuming 10 as the threshold
                Order.objects.create(
                    spare_part=spare_part,
                    quantity=random.randint(1, 50),
                    expected_delivery_date=fake.future_date(),
                )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
