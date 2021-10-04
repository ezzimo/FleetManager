import datetime

import vehicle
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.db.models import F, Sum
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.views import View, generic
from django.views.generic.dates import (
    TodayArchiveView,
    WeekArchiveView,
    YearArchiveView,
)
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from vehicle.models import Vehicle

from refuel.models import GazStation

from .forms import RefuelChangeForm, RefuelCreationForm
from .models import FuelConsumption, Refuel

year, week, _ = now().isocalendar()

###########################################################################################
###################### GazStation Views   #################################################
###########################################################################################


class GazStationsListView(LoginRequiredMixin, generic.ListView):
    """GazStationListView: produce a list of all GazStation"""

    model = GazStation
    paginate_by = 15


class GazStationCreationView(LoginRequiredMixin, CreateView):
    model = GazStation
    fields = "__all__"
    success_url = reverse_lazy("refuel:all-gazstations")


class GazStationUpdateView(LoginRequiredMixin, UpdateView):
    model = GazStation
    fields = "__all__"
    success_url = reverse_lazy("refuel:all-gazstations")


class GazStationDeleteView(LoginRequiredMixin, DeleteView):
    model = GazStation
    fields = "__all__"
    success_url = reverse_lazy("refuel:all-gazstations")


###########################################################################################
###################### Refuel Views   #####################################################
###########################################################################################


class RefuelsListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """RefuelsListView: produce a list of all Refuels"""

    model = Refuel
    queryset = Refuel.objects.order_by("-created_at").all()
    success_url = reverse_lazy("")
    template_name = "refuel/supervisor/refuel_list.html"
    allow_empty = True
    redirect_field_name = ""
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super(RefuelsListView, self).get_context_data(**kwargs)
        context["Totale"] = (
            Refuel.objects.values("gaz_station")
            .order_by("gaz_station")
            .annotate(total=Sum(F("fuel_quantity") * F("fuel_unit_price")))
        )
        if context["Totale"]:
            return context
        elif not context["Totale"]:
            context["Totale"] = 0
            return context

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_supervisor


class RefuelCreationView(LoginRequiredMixin, CreateView):
    model = Refuel
    form_class = RefuelCreationForm
    template_name = "refuel/refuel_form.html"
    success_url = reverse_lazy("refuel:controlor-refuel-list")

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.gaz_station = GazStation.objects.get(Controlor_id=self.request.user.id)
        old_refuel_data = Refuel.objects.order_by().distinct("vehicle")
        for refuel in old_refuel_data:
            if refuel.vehicle == form.instance.vehicle and form.instance.odometer_reading:
                consumption = (refuel.fuel_quantity / (form.instance.odometer_reading - refuel.odometer_reading)) * 100
                FuelConsumption.objects.create(
                    vehicle=refuel.vehicle,
                    gaz_station=form.instance.gaz_station,
                    Controlor_id=self.request.user,
                    driver=refuel.vehicle.driver,
                    consumption=consumption,
                    is_active=True,
                )
            elif refuel.vehicle == form.instance.vehicle and form.instance.snitch:
                consumption = (refuel.fuel_quantity / (form.instance.snitch - refuel.snitch)) * 100
                FuelConsumption.objects.create(
                    vehicle=refuel.vehicle,
                    gaz_station=form.instance.gaz_station,
                    Controlor_id=self.request.user,
                    driver=refuel.vehicle.driver,
                    consumption=consumption,
                    is_active=True,
                )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"].fields["vehicle"].queryset = Vehicle.objects.select_related(
            "gaz_station__Controlor_id"
        ).filter(gaz_station__Controlor_id=self.request.user)
        return context

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_controlor


class RefuelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Refuel
    form_class = RefuelChangeForm
    success_url = reverse_lazy("refuel:controlor-refuel-list")

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_controlor


class RefuelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Refuel
    fields = "__all__"
    success_url = reverse_lazy("refuel:controlor-refuel-list")

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_controlor


####### refuel view filtred by year  #################
class RefuelsListViewSup(LoginRequiredMixin, YearArchiveView):
    queryset = Refuel.objects.order_by("vehicle_id").all()
    date_field = "created_at"
    make_object_list = True
    allow_future = True


#### Controlor view for refuel list of the day


class ControlorRefuel(LoginRequiredMixin, UserPassesTestMixin, WeekArchiveView):
    """ControlorRefuel: produce a View for Controlor"""

    model = Refuel
    date_field = "created_at"
    template_name = "refuel/controlor/controlor_today.html"
    context_object_name = "todayrefuel"
    week_format = "%W"
    week = week
    year = year
    queryset = Refuel.objects.select_related("gaz_station__Controlor_id")
    allow_empty = True

    def get_queryset(self, **kwargs):
        queryset = self.queryset.filter(gaz_station__Controlor_id=self.request.user.id)
        return queryset

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_controlor


###########################################################################################
###################### Fuel Consumption Views   #####################################################
###########################################################################################


class FuelConsumptionView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """FuelConsumptionView: produce a list of all Fuel Consumption per Refuel"""

    model = FuelConsumption
    queryset = FuelConsumption.objects.all()
    success_url = reverse_lazy("")
    template_name = "refuel/supervisor/fuel_consumption_list.html"
    allow_empty = True
    redirect_field_name = ""
    paginate_by = 40

    def test_func(self):
        return self.request.user.is_active and self.request.user.is_supervisor
