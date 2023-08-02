from .factories import SparePartFactory

def test_spare_part_factory():
    spare_part = SparePartFactory()
    assert spare_part.name is not None
    assert spare_part.description is not None
    assert spare_part.quantity is not None
