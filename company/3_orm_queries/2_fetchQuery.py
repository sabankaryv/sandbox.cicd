# ============================================================
# DJANGO ORM - FETCH / RETRIEVAL METHODS
# ============================================================

import os
import sys
import django


# ============================================================
# DJANGO SETUP
# ============================================================

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "company.settings"
)

django.setup()

from employee.models import Employee, Department


# ============================================================
# ORM METHODS - MEMORY TRICK
# ============================================================

"""
ALL        == all()
GOOD       == get()
FRIENDS    == filter()
EAT        == exclude()
VEGETABLES == values()
VERY       == values_list()
OFTEN      == only()
DURING     == defer()
FESTIVALS  == first()
LUNCH      == last()
EVENING    == exists()
COFFEE     == count()
BROCCOLI   == in_bulk()


Memory Sentence:

"ALL GOOD FRIENDS EAT VEGETABLES VERY OFTEN
 DURING FESTIVALS, LUNCH, EVENING, COFFEE, BROCCOLI."
"""


# ============================================================
# GET DEPARTMENT
# ============================================================

department = Department.objects.get(id=1)

print("\n================ DEPARTMENT ================")

print(f"ID   : {department.id}")
print(f"Name : {department.name}")

# OUTPUT:
#
# ================ DEPARTMENT ================
# ID   : 1
# Name : Finance


# ============================================================
# 1. ALL - Using all()
# ============================================================

print("\n================ 1. ALL ====================")

employees = Employee.objects.all()

for emp in employees:
    print(
        emp.id,
        emp.name,
        emp.email,
        emp.salary,
        emp.department,
        emp.age,
        emp.status
    )

# OUTPUT:
#
# 3  Test User  test@example.com      50000.00  Finance  30  active
# 8  Rahul      sabankaryw@gmail.com  50000.00  Finance  25  active
# 10 Yogesh     sabana@gmail.com       30000.00  Finance  30  active
# 11 sachin     abc@gmail.com          40000.00  Finance  25  active
# 12 Ishan      ishan@gmail.com        70000.00  Finance  22  active
# 13 Sanju      sanju@gmail.com         6777.00  Finance  30  active
# 14 Rahul      rahul@gmail.com        50000.00  Finance  25  active
# 15 Yogesh     yogesh@gmail.com       30000.00  Finance  30  active
# 16 Sachin     sachin@gmail.com       40000.00  Finance  25  active
#
# Return:
# QuerySet


# ============================================================
# 2. GET - Using get()
# ============================================================

print("\n================ 2. GET ====================")

employee = Employee.objects.get(id=3)

print(employee.id, type(employee))

# OUTPUT:
#
# 3 <class 'employee.models.Employee'>
#
# Return:
# Single Employee object


# ============================================================
# 3. FILTER - Using filter()
# ============================================================

print("\n================ 3. FILTER =================")

employees = Employee.objects.filter(id=3)

for emp in employees:
    print(
        emp.id,
        emp.name,
        emp.email,
        emp.salary,
        emp.department,
        emp.age,
        emp.status
    )

# OUTPUT:
#
# 3 Test User test@example.com 50000.00 Finance 30 active
#
# Return:
# QuerySet


# ============================================================
# 4. EXCLUDE - Using exclude()
# ============================================================

print("\n================ 4. EXCLUDE ================")

employees = Employee.objects.exclude(id=4)

for emp in employees:
    print(
        emp.id,
        emp.name,
        emp.email,
        emp.salary,
        emp.department,
        emp.age,
        emp.status
    )

# OUTPUT:
#
# 3  Test User  test@example.com      50000.00 Finance 30 active
# 8  Rahul      sabankaryw@gmail.com  50000.00 Finance 25 active
# 10 Yogesh     sabana@gmail.com       30000.00 Finance 30 active
# 11 sachin     abc@gmail.com          40000.00 Finance 25 active
# 12 Ishan      ishan@gmail.com        70000.00 Finance 22 active
# 13 Sanju      sanju@gmail.com         6777.00 Finance 30 active
# 14 Rahul      rahul@gmail.com        50000.00 Finance 25 active
# 15 Yogesh     yogesh@gmail.com       30000.00 Finance 30 active
# 16 Sachin     sachin@gmail.com       40000.00 Finance 25 active
#
# Return:
# QuerySet


# ============================================================
# 5. VALUES - Using values()
# ============================================================

print("\n================ 5. VALUES =================")

employees = Employee.objects.values()

print(type(employees))

for emp in employees:
    print(emp["id"])

# OUTPUT:
#
# <class 'django.db.models.query.QuerySet'>
#
# 3
# 8
# 10
# 11
# 12
# 13
# 14
# 15
# 16
#
# Return:
# QuerySet
#
# Each item:
# Dictionary


# ============================================================
# 6. VALUES_LIST - Using values_list()
# ============================================================

print("\n================ 6. VALUES_LIST ===========")

employees = Employee.objects.values_list()

print(type(employees))

for emp in employees:
    print(emp)

# OUTPUT:
#
# <class 'django.db.models.query.QuerySet'>
#
# (3, 'Test User', 'test@example.com', Decimal('50000.00'),
#  1, 30, 'active', ...)
#
# (8, 'Rahul', 'sabankaryw@gmail.com', Decimal('50000.00'),
#  1, 25, 'active', ...)
#
# (10, 'Yogesh', 'sabana@gmail.com', Decimal('30000.00'),
#  1, 30, 'active', ...)
#
# ...
#
# Return:
# QuerySet
#
# Each item:
# Tuple


# ============================================================
# 7. ONLY - Using only()
# ============================================================

print("\n================ 7. ONLY ==================")

employees = Employee.objects.only(
    "id",
    "name",
    "salary"
)

for emp in employees:
    print(
        emp.id,
        emp.name,
        emp.salary
    )

# OUTPUT:
#
# 3 Test User 50000.00
# 8 Rahul 50000.00
# 10 Yogesh 30000.00
# 11 sachin 40000.00
# 12 Ishan 70000.00
# 13 Sanju 6777.00
# 14 Rahul 50000.00
# 15 Yogesh 30000.00
# 16 Sachin 40000.00
#
# Return:
# QuerySet of Employee objects


# ============================================================
# 8. DEFER - Using defer()
# ============================================================

print("\n================ 8. DEFER =================")

employees = Employee.objects.defer(
    "email",
    "salary"
)

for emp in employees:
    print(
        emp.id,
        emp.name
    )

# OUTPUT:
#
# 3 Test User
# 8 Rahul
# 10 Yogesh
# 11 sachin
# 12 Ishan
# 13 Sanju
# 14 Rahul
# 15 Yogesh
# 16 Sachin
#
# Return:
# QuerySet of Employee objects
#
# email and salary are initially deferred


# ============================================================
# 9. FIRST - Using first()
# ============================================================

print("\n================ 9. FIRST =================")

employee = Employee.objects.first()

print("Employee:", employee)
print("Type:", type(employee))

# OUTPUT:
#
# Employee: Test User
# Type: <class 'employee.models.Employee'>
#
# Return:
# Single Employee object
#
# If no records:
# None


# ============================================================
# 10. LAST - Using last()
# ============================================================

print("\n================ 10. LAST =================")

employee = Employee.objects.last()

print("Employee:", employee)
print("Type:", type(employee))

# OUTPUT:
#
# Employee: Sachin
# Type: <class 'employee.models.Employee'>
#
# Return:
# Single Employee object
#
# If no records:
# None


# ============================================================
# 11. EXISTS - Using exists()
# ============================================================

print("\n================ 11. EXISTS ===============")

employee_exists = Employee.objects.filter(id=3).exists()

print(employee_exists)

# OUTPUT:
#
# True
#
# Return:
# Boolean
#
# True  -> Record exists
# False -> Record does not exist


# ============================================================
# 12. COUNT - Using count()
# ============================================================

print("\n================ 12. COUNT ================")

employee_count = Employee.objects.count()

print(employee_count)

# OUTPUT:
#
# 9
#
# Return:
# Integer


# ============================================================
# 13. IN_BULK - Using in_bulk()
# ============================================================

print("\n================ 13. IN_BULK ==============")

employees = Employee.objects.in_bulk(
    [3, 8, 10]
)

print(employees)

# OUTPUT:
#
# {
#     3: <Employee: Test User>,
#     8: <Employee: Rahul>,
#     10: <Employee: Yogesh>
# }
#
# Return:
# Dictionary
#
# Key   -> Employee ID
# Value -> Employee object