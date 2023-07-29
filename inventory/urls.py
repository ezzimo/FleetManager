from django.urls import path
from .views import SparePartsListView, SparePartDetailView, SparePartCreateView, SparePartUpdateView, SparePartDeleteView

app_name = 'inventory'
urlpatterns = [
    path('spare_parts/', SparePartsListView.as_view(), name='spare_parts_list'),
    path('spare_part/<int:pk>/', SparePartDetailView.as_view(), name='spare_part_detail'),
    path('spare_part/new/', SparePartCreateView.as_view(), name='spare_part_new'),
    path('spare_part/<int:pk>/edit/', SparePartUpdateView.as_view(), name='spare_part_edit'),
    path('spare_part/<int:pk>/delete/', SparePartDeleteView.as_view(), name='spare_part_delete'),
]
