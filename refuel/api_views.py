from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import FuelConsumption, Refuel
from .serializers import ConsumptionSerializer, RefuelSerializer


class RefuelViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Refuel.objects.all()
    serializer_class = RefuelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RefuelSerializer(queryset, many=True)
        return Response(serializer.data)


class ConsumptionViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = FuelConsumption.objects.all()
    serializer_class = ConsumptionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ConsumptionSerializer(queryset, many=True)
        return Response(serializer.data)
