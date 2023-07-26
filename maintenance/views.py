from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MaintenanceRecord
from .forms import MaintenanceRecordForm
from account.decorators import AdministrationOnlyMixin
from django.utils.decorators import method_decorator


class MaintenanceRecordListView(AdministrationOnlyMixin, ListView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_list.html'  # Adjust as needed
    context_object_name = 'records'


class MaintenanceRecordDetailView(AdministrationOnlyMixin, DetailView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_detail.html'  # Adjust as needed
    context_object_name = 'record'


class MaintenanceRecordCreateView(AdministrationOnlyMixin, CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'maintenance/maintenance_record_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance_record_detail', args=[self.object.id])


class MaintenanceRecordUpdateView(AdministrationOnlyMixin, UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'maintenance/maintenance_record_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance_record_detail', args=[self.object.id])


class MaintenanceRecordDeleteView(AdministrationOnlyMixin, DeleteView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_confirm_delete.html'  # Adjust as needed

    def get_success_url(self):
        return reverse_lazy('maintenance_record_list')
