from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MaintenanceRecord
from .forms import MaintenanceRecordForm


class MaintenanceRecordListView(ListView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_list.html'  # Adjust as needed
    context_object_name = 'records'


class MaintenanceRecordDetailView(DetailView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_detail.html'  # Adjust as needed
    context_object_name = 'record'


class MaintenanceRecordCreateView(CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'maintenance/maintenance_record_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance_record_detail', args=[self.object.id])


class MaintenanceRecordUpdateView(UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'maintenance/maintenance_record_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance_record_detail', args=[self.object.id])


class MaintenanceRecordDeleteView(DeleteView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_confirm_delete.html'  # Adjust as needed

    def get_success_url(self):
        return reverse_lazy('maintenance_record_list')
