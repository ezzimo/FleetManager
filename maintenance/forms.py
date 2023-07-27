from django import forms
from django.core.validators import MinValueValidator
from .models import MaintenanceSchedule, MaintenanceRecord, MaintenanceType
from vehicle.models import Vehicle


class MaintenanceScheduleFilterForm(forms.Form):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)
    maintenance_type = forms.ModelChoiceField(queryset=MaintenanceType.objects.all(), required=False)


class MaintenanceRecordFilterForm(forms.Form):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=False)
    maintenance_type = forms.ModelChoiceField(queryset=MaintenanceType.objects.all(), required=False)
    date = forms.DateField(required=False)



class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSchedule
        fields = ['vehicle', 'maintenance_type', 'scheduled_date', 'notes']


class MaintenanceRecordForm(forms.ModelForm):
    cost = forms.DecimalField(validators=[MinValueValidator(0)])

    class Meta:
        model = MaintenanceRecord
        fields = ('vehicle', 'date', 'maintenance_type', 'notes', 'cost')
