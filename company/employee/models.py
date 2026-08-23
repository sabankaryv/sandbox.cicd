from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)

class EmployeeStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    ON_LEAVE = "on_leave", "On Leave"
    RESIGNED = "resigned", "Resigned"


class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    age = models.IntegerField()
    status=models.CharField(max_length=20,choices=EmployeeStatus.choices,default=EmployeeStatus.ACTIVE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)