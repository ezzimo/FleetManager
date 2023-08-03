from django import forms
from .models import Company, Employee

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_details', 'number_of_employees', 'fleet_size']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'contact_details', 'company', 'role']
