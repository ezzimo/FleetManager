from rest_framework import viewsets, filters
from .models import SparePart
from .serializers import SparePartSerializer

class SparePartViewSet(viewsets.ModelViewSet):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
