from django.urls import path
from .views import (
    MaintenanceRecordListView,
    MaintenanceRecordDetailView,
    MaintenanceRecordCreateView,
    MaintenanceRecordUpdateView,
    MaintenanceRecordDeleteView,
)

app_name = "maintenance"

urlpatterns = [
    path('list/', MaintenanceRecordListView.as_view(), name='maintenance_record_list'),
    path('<int:pk>/', MaintenanceRecordDetailView.as_view(), name='maintenance_record_detail'),
    path('new/', MaintenanceRecordCreateView.as_view(), name='maintenance_record_new'),
    path('<int:pk>/edit/', MaintenanceRecordUpdateView.as_view(), name='maintenance_record_edit'),
    path('<int:pk>/delete/', MaintenanceRecordDeleteView.as_view(), name='maintenance_record_delete'),
]
