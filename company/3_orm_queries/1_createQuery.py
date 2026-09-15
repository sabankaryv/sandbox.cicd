import os
import sys
import django

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company.settings")
django.setup()
from employee.models import Employee, Department


# 1_createQuery.py
# ============================================================
# DJANGO ORM - CREATE OBJECTS
# ============================================================

import os
import sys
import django

# ------------------------------------------------------------
# Django Setup
# ------------------------------------------------------------

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "company.settings"
)

django.setup()

from employee.models import Employee, Department


# ============================================================
# 1. GET DEPARTMENT
# ============================================================

department = Department.objects.get(id=1)

print("\nDepartment:")
print(f"  ID   : {department.id}")
print(f"  Name : {department.name}")


# ============================================================
# 2. CREATE - Using create()
# ============================================================

employee = Employee.objects.create(
    name="Rahul",
    age=25,
    salary=50000,
    email="rahul@gmail.com",
    status="active",
    department=department
)

print("\n1. create()")
print("   Employee created:", employee)


# ============================================================
# 3. CREATE - Using save()
# ============================================================

employee2 = Employee(
    name="Yogesh",
    age=30,
    salary=30000,
    email="yogesh@gmail.com",
    status="active",
    department=department
)

employee2.save()

print("\n2. save()")
print("   Employee created:", employee2)


# ============================================================
# 4. CREATE - Using get_or_create()
# ============================================================

employee3, created = Employee.objects.get_or_create(
    email="sachi1n@gmail.com",
    defaults={
        "name": "Sachin",
        "age": 25,
        "salary": 40000,
        "status": "active",
        "department": department,
    }
)

print("\n3. get_or_create()")
print("   Employee:", employee3)
print("   Created :", created)


# ============================================================
# 5. CREATE - Using bulk_create()
# ============================================================

employees = [
    Employee(
        name="Ishan",
        age=22,
        salary=70000,
        email="ishan@gmail.com",
        status="active",
        department=department,
    ),
    Employee(
        name="Sanju",
        age=30,
        salary=6777,
        email="sanju@gmail.com",
        status="active",
        department=department,
    ),
]

created_employees = Employee.objects.bulk_create(employees)

print("\n4. bulk_create()")

for employee in created_employees:
    print(
        f"   Created: "
        f"{employee.name} | "
        f"{employee.email}"
    )


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("CREATE OPERATIONS COMPLETED")
print("CSGB → “Create, Save, Get, Batch")
print("=" * 60)

print("""
1. create()        → Create one object directly
2. save()          → Create object and explicitly save
3. get_or_create() → Get existing OR create new
4. bulk_create()   → Create multiple objects at once
""")