from django.contrib.admin.sites import AdminSite
from inventory.admin import SparePartAdmin
from inventory.models import SparePart
from .factories import SparePartFactory

class MockRequest:
    pass

request = MockRequest()

def test_spare_part_admin():
    site = AdminSite()
    admin = SparePartAdmin(SparePart, site)
    spare_part = SparePartFactory()
    assert admin.get_queryset(request)[0] == spare_part
