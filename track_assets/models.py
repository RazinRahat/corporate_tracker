from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.name}")

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return(f"{self.name}")

class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return(f"{self.name}")

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return(f"{self.checkout_date}")