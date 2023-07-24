from account.models import City, User
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _


class GazStation(models.Model):
    name = models.CharField(max_length=128, blank=True, unique=True)
    Controlor_id = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        limit_choices_to={"is_controlor": True, "is_active": True},
    )
    city_id = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    geo_localization = gis_models.PointField(blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["city_id", "name"]

    def __str__(self):
        return "%s %s" % (self.name, self.city_id.city)


class Refuel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name=_("responsable_user"), default=1)
    vehicle = models.ForeignKey("vehicle.Vehicle", blank=True, null=True, on_delete=models.PROTECT)
    gaz_station = models.ForeignKey(
        GazStation, related_name=_("Refuel_Station"), blank=True, null=True, on_delete=models.PROTECT
    )
    odometer_reading = models.PositiveIntegerField(_("Compteur KM"), blank=True, null=True)
    snitch = models.PositiveIntegerField(_("Mouchard KM"), blank=True, null=True)
    fuel_quantity = models.DecimalField(_("Quantitée en Litres"), max_digits=5, decimal_places=1)
    fuel_unit_price = models.DecimalField(_("Prix en DH"), max_digits=6, decimal_places=2)
    note = models.CharField(_("Remarque"), max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def total_price(self):
        total_price = self.fuel_quantity * self.fuel_unit_price
        return total_price

    class Meta:
        ordering = ["gaz_station", "-created_at"]
        get_latest_by = "created_at"

    def __str__(self):
        return self.vehicle.serie


class FuelConsumption(models.Model):
    vehicle = models.ForeignKey("vehicle.Vehicle", blank=True, null=True, on_delete=models.PROTECT)
    gaz_station = models.ForeignKey(
        GazStation, related_name=_("Station_consuption"), blank=True, null=True, on_delete=models.PROTECT
    )
    Controlor_id = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        limit_choices_to={"is_controlor": True, "is_active": True},
    )
    driver = models.ForeignKey(
        User, related_name=_("Vehicle_Driver_consuption"), blank=True, null=True, on_delete=models.PROTECT
    )
    consumption = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at", "vehicle"]

    def __str__(self):
        return self.vehicle.serie
