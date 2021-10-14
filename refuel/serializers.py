from django.db.models import fields
from rest_framework import serializers
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated

from .models import FuelConsumption, Refuel


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class RefuelSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated | ReadOnly]
    vehicle = serializers.StringRelatedField()
    gaz_station = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Refuel
        fields = "__all__"


class ConsumptionSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    gaz_station = serializers.StringRelatedField()
    Controlor_id = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()

    class Meta:
        model = FuelConsumption
        fields = "__all__"
