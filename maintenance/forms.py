from django import forms
from .models import MaintenanceRecord

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ('vehicle', 'date', 'maintenance_type', 'notes', 'cost')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the form rendering
        self.fields['vehicle'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['maintenance_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()

        # Customize the error handling
        vehicle = cleaned_data.get('vehicle')
        date = cleaned_data.get('date')
        maintenance_type = cleaned_data.get('maintenance_type')
        cost = cleaned_data.get('cost')

        if not vehicle:
            self.add_error('vehicle', 'Vehicle is required.')
        if not date:
            self.add_error('date', 'Date is required.')
        if not maintenance_type:
            self.add_error('maintenance_type', 'Maintenance type is required.')
        if cost is None or cost < 0:
            self.add_error('cost', 'Cost must be a positive number.')
