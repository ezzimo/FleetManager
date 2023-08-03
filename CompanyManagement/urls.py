from django.urls import path
from .views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView, EmployeeDetailView, EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView


app_name = "company_management"


urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('company/new/', CompanyCreateView.as_view(), name='company_new'),
    path('company/<int:pk>/edit/', CompanyUpdateView.as_view(), name='company_edit'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/new/', EmployeeCreateView.as_view(), name='employee_new'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]
