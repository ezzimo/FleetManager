from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import (
    AnssuranceCompany,
    AnssuranceType,
    Make,
    ModelSpecificationValue,
    Vehicle,
    VehicleHome,
    VehicleModel,
)


def vehicle_home(request):
    vehicles = VehicleHome.objects.prefetch_related("model")
    return render(request, "vehicle/home.html", {"vehicles": vehicles})


@login_required
def vehicle_detail(request, slug):
    vehicle = get_object_or_404(Vehicle, slug=slug)
    specifications = ModelSpecificationValue.objects.filter(vehicle=vehicle)
    return render(request, "vehicle/vehicle.html", {"vehicle": vehicle, "specifications": specifications})


@login_required
def vehicle_all(request):
    vehicles = Vehicle.objects.prefetch_related("model")
    return render(request, "vehicle/vehicles.html", {"vehicles": vehicles})


######################################################################################
#######################   Vehicle Model        ######################################
######################################################################################


class VehicleCreationView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    fields = "__all__"
    success_url = reverse_lazy("vehicle:vehicles_all")

    def test_func(self):
        return (self.request.user.is_exploitation or self.request.user.is_supervisor) and self.request.user.is_active


class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    fields = "__all__"
    success_url = reverse_lazy("vehicle:vehicles_all")

    def test_func(self):
        return (self.request.user.is_exploitation or self.request.user.is_supervisor) and self.request.user.is_active


class VehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vehicle
    fields = "__all__"
    success_url = reverse_lazy("vehicle:vehicles_all")

    def test_func(self):
        return (
            self.request.user.is_exploitation or self.request.user.is_planification
        ) and self.request.user.is_active
