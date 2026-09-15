from django.contrib import admin
from .models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "salary",
        "department",
        "age",
        "status",
        "created_at",
        "updated_at",
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "location",
        "manager",
        "budget"
    )