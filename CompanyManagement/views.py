from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Company, Employee
from .forms import CompanyForm, EmployeeForm


class CompanyListView(ListView):
    model = Company
    template_name = 'company_management/company_list.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_management/company_detail.html'
    context_object_name = 'company'


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company_management/company_form.html'
    form_class = CompanyForm
    success_url = reverse_lazy('company_management:company_list')


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'company_management/company_form.html'
    form_class = CompanyForm
    success_url = reverse_lazy('company_management:company_list')


class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_management/company_confirm_delete.html'
    success_url = reverse_lazy('company_management:company_list')


class EmployeeListView(ListView):
    model = Company
    template_name = 'company_management/employee_list.html'
    context_object_name = 'employees'


class EmployeeDetailView(DetailView):
    model = Company
    template_name = 'company_management/employee_detail.html'
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = Company
    template_name = 'company_management/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('company_management:employee_list')


class EmployeeUpdateView(UpdateView):
    model = Company
    template_name = 'company_management/.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('company_management:employee_list')


class EmployeeDeleteView(DeleteView):
    model = Company
    template_name = 'company_management/employee_confirm_delete.html'
    success_url = reverse_lazy('company_management:company_list')
