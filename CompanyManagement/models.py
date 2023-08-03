from django.db import models
from account.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    fleet_size = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    contact_details = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name
