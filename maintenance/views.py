from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MaintenanceSchedule, MaintenanceRecord
from .forms import MaintenanceScheduleForm, MaintenanceRecordForm, MaintenanceRecordFilterForm, MaintenanceScheduleFilterForm
from account.decorators import AdministrationOnlyMixin


class MaintenanceScheduleListView(AdministrationOnlyMixin, ListView):
    model = MaintenanceSchedule
    template_name = 'maintenance/maintenance_schedule_list.html'
    context_object_name = 'schedules'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = MaintenanceScheduleFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().select_related('vehicle', 'maintenance_type')
        filter_form = MaintenanceScheduleFilterForm(self.request.GET)
        if self.request.GET and filter_form.is_valid():
            # Apply filters to the queryset based on the form data
            if filter_form.cleaned_data['vehicle']:
                queryset = queryset.filter(vehicle=filter_form.cleaned_data['vehicle'])
            if filter_form.cleaned_data['maintenance_type']:
                queryset = queryset.filter(maintenance_type=filter_form.cleaned_data['maintenance_type'])
        return queryset


class MaintenanceScheduleCreateView(AdministrationOnlyMixin, CreateView):
    model = MaintenanceSchedule
    form_class = MaintenanceScheduleForm
    template_name = 'maintenance/maintenance_schedule_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance:maintenance_schedule_detail', args=[self.object.id])


class MaintenanceScheduleDetailView(AdministrationOnlyMixin, DetailView):
    model = MaintenanceSchedule
    template_name = 'maintenance/maintenance_schedule_detail.html'
    context_object_name = 'schedule'


class MaintenanceScheduleUpdateView(AdministrationOnlyMixin, UpdateView):
    model = MaintenanceSchedule
    form_class = MaintenanceScheduleForm
    template_name = 'maintenance/maintenance_schedule_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance:maintenance_schedule_detail', args=[self.object.id])


class MaintenanceScheduleDeleteView(AdministrationOnlyMixin, DeleteView):
    model = MaintenanceSchedule
    template_name = 'maintenance/maintenance_schedule_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('maintenance:maintenance_schedule_list')


class MaintenanceRecordListView(AdministrationOnlyMixin, ListView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_list.html'
    context_object_name = 'records'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = MaintenanceRecordFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().select_related('vehicle', 'maintenance_type')
        filter_form = MaintenanceRecordFilterForm(self.request.GET)
        if self.request.GET and filter_form.is_valid():
            # Apply filters to the queryset based on the form data
            if filter_form.cleaned_data['vehicle']:
                queryset = queryset.filter(vehicle=filter_form.cleaned_data['vehicle'])
            if filter_form.cleaned_data['maintenance_type']:
                queryset = queryset.filter(maintenance_type=filter_form.cleaned_data['maintenance_type'])
            if filter_form.cleaned_data['date']:
                queryset = queryset.filter(date=filter_form.cleaned_data['date'])
        return queryset



class MaintenanceRecordDetailView(AdministrationOnlyMixin, DetailView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_detail.html'  # Adjust as needed
    context_object_name = 'record'


class MaintenanceRecordCreateView(AdministrationOnlyMixin, CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'maintenance/maintenance_record_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance:maintenance_record_detail', args=[self.object.id])


class MaintenanceRecordUpdateView(AdministrationOnlyMixin, UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceRecordForm
    template_name = 'maintenance/maintenance_record_form.html'

    def get_success_url(self):
        return reverse_lazy('maintenance:maintenance_record_detail', args=[self.object.id])


class MaintenanceRecordDeleteView(AdministrationOnlyMixin, DeleteView):
    model = MaintenanceRecord
    template_name = 'maintenance/maintenance_record_confirm_delete.html'  # Adjust as needed

    def get_success_url(self):
        return reverse_lazy('maintenance:maintenance_record_list')
