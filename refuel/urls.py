from django import urls
from django.db import router
from django.urls import include, path

from . import views

app_name = "refuel"

urlpatterns = [
    path("gazstations", views.GazStationsListView.as_view(), name="all-gazstations"),
    path("GazStationCreation", views.GazStationCreationView.as_view(), name="gazstation-creation"),
    path("<int:pk>/GazStationUpdate", views.GazStationUpdateView.as_view(), name="gazstation-update"),
    path("<int:pk>GazStationDeletion", views.GazStationDeleteView.as_view(), name="gazstation-delete"),
    path("refuels", views.RefuelsListView.as_view(), name="all-refuels"),
    path("<int:year>/", views.RefuelsListViewSup.as_view(), name="refuel_year_archive"),
    path("RefuelCreation", views.RefuelCreationView.as_view(), name="refuel-creation"),
    path("<int:pk>RefuelUpdate", views.RefuelUpdateView.as_view(), name="refuel-update"),
    path("<int:pk>RefuelDeletion", views.RefuelDeleteView.as_view(), name="refuel-delete"),
    path("ControlorRefuelList", views.ControlorRefuel.as_view(), name="controlor-refuel-list"),
    path("consumption", views.FuelConsumptionView.as_view(), name="consumption"),
]
