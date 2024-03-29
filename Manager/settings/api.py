from refuel import api_views as refuel_views
from inventory import api_views as inventory_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"refuels", refuel_views.RefuelViewSet, "refuels")
router.register(r"consumption", refuel_views.ConsumptionViewSet, "consumption")
router.register(r"inventory", inventory_views.SparePartViewSet, "inventory")
# router.register(r'borrowings', refuel_views.BorrowedViewset)
