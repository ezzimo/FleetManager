from django.db.models import fields
from rest_framework import serializers

from .models import FuelConsumption, Refuel


class RefuelSerializer(serializers.ModelSerializer):
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
