from django import forms
from django.contrib.gis import forms
from django.db.models import fields
from django.forms import widgets

from .models import *


class GazStationCreationForm(forms.ModelForm):
    class Meta:
        model = GazStation
        fields = "__all__"
        widgets = {
            "geo_localization": forms.OSMWidget(attrs={"map_width": 800, "map_height": 500}),
        }


###########################################################################################
########################## Refuel Forms     ############################################
###########################################################################################
class RefuelCreationForm(forms.ModelForm):
    class Meta:
        model = Refuel
        fields = (
            "vehicle",
            "odometer_reading",
            "snitch",
            "fuel_quantity",
            "fuel_unit_price",
            "note",
        )
        widgets = {
            "vehicle": forms.Select(
                attrs={"class": "form-control mb-2 refuel-form", "placeholder": "Select un vehicule"},
            ),
            "odometer_reading": forms.NumberInput(),
            "snitch": forms.NumberInput(),
            "fuel_quantity": forms.NumberInput(),
            "fuel_unit_price": forms.NumberInput,
            "note": forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["vehicle"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "id": "vehicle-select", "Placeholder": "vehicule"}
        )
        self.fields["odometer_reading"].widget.attrs.update(
            {"class": "form-control mb-2 refuel-form", "id": "odometer", "Placeholder": "Compteur"}
        )
        self.fields["snitch"].widget.attrs.update(
            {"class": "form-control mb-2 refuel-form", "Placeholder": "mouchard"}
        )
        self.fields["fuel_quantity"].widget.attrs.update(
            {"class": "form-control mb-2 refuel-form", "id": "fuel_qty", "Placeholder": "litrage"}
        )
        self.fields["fuel_unit_price"].widget.attrs.update(
            {"class": "form-control mb-2 refuel-form", "Placeholder": "prix unitaire"}
        )
        self.fields["note"].widget.attrs.update({"class": "form-control mb-2 refuel-form", "Placeholder": "remarque"})


class RefuelChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = Refuel
        fields = (
            "vehicle",
            "gaz_station",
            "odometer_reading",
            "snitch",
            "fuel_quantity",
            "fuel_unit_price",
            "note",
        )
