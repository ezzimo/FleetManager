import factory
from inventory.models import SparePart

class SparePartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SparePart

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    quantity = factory.Faker('random_int')
