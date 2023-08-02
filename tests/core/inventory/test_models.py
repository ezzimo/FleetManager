from inventory.models import SparePart
from .factories import SparePartFactory

def test_spare_part_creation():
    spare_part = SparePartFactory()
    assert isinstance(spare_part, SparePart)
    assert spare_part.name is not None
    assert spare_part.description is not None
    assert spare_part.quantity is not None
