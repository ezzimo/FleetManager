from django.urls import path
from .views import (
    MaintenanceRecordListView,
    MaintenanceRecordDetailView,
    MaintenanceRecordCreateView,
    MaintenanceRecordUpdateView,
    MaintenanceRecordDeleteView,
    MaintenanceScheduleListView,
    MaintenanceScheduleDetailView,
    MaintenanceScheduleCreateView,
    MaintenanceScheduleUpdateView,
    MaintenanceScheduleDeleteView,
)

app_name = "maintenance"

urlpatterns = [
    path('records/list/', MaintenanceRecordListView.as_view(), name='maintenance_record_list'),
    path('records/<int:pk>/', MaintenanceRecordDetailView.as_view(), name='maintenance_record_detail'),
    path('records/new/', MaintenanceRecordCreateView.as_view(), name='maintenance_record_new'),
    path('records/<int:pk>/edit/', MaintenanceRecordUpdateView.as_view(), name='maintenance_record_edit'),
    path('records/<int:pk>/delete/', MaintenanceRecordDeleteView.as_view(), name='maintenance_record_delete'),
    path('schedules/', MaintenanceScheduleListView.as_view(), name='maintenance_schedule_list'),
    path('schedules/<int:pk>/', MaintenanceScheduleDetailView.as_view(), name='maintenance_schedule_detail'),
    path('schedules/new/', MaintenanceScheduleCreateView.as_view(), name='new_maintenance_schedule'),
    path('schedules/<int:pk>/edit/', MaintenanceScheduleUpdateView.as_view(), name='update_maintenance_schedule'),
    path('schedules/<int:pk>/delete/', MaintenanceScheduleDeleteView.as_view(), name='delete_maintenance_schedule'),
]
