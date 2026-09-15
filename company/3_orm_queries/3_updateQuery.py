# ============================================================
# DJANGO ORM - UPDATE METHODS
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
from django.db.models import F


# ============================================================
# ORM METHODS - MEMORY TRICK
# ============================================================

"""
Memory Sentence:

"SAVE UPDATE UPDATE_OR_CREATE F BULK_UPDATE"

SAVE
→ Update one model object

UPDATE
→ Update one or many database rows

UPDATE_OR_CREATE
→ Update if exists, otherwise create

F
→ Database-side calculation

BULK_UPDATE
→ Update multiple existing objects together
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
# 1. SAVE - Using save()
# ============================================================

print("\n================ 1. SAVE ===================")

employee = Employee.objects.get(id=3)

employee.name = "AB Bhai"

employee.save()

print(employee.id)
print(employee.name)

# OUTPUT:
#
# 3
# AB Bhai


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

"""
save() is generally used when we have a model object
and want to save changes made to that object.

Step 1:
    Get object
    employee = Employee.objects.get(id=3)

Step 2:
    Change field
    employee.name = "AB Bhai"

Step 3:
    Save changes
    employee.save()
Before:
    ID = 3
    Name = Test User
After:
    ID = 3
    Name = AB Bhai
Return:
    save() returns None

Important:
    get()       -> Employee object
    save()      -> saves changes to database
"""


# ============================================================
# 2. UPDATE - Using update()
# ============================================================

print("\n================ 2. UPDATE =================")

updated_count = Employee.objects.filter(
    department_id=1
).update(
    salary=70000
)

print("Updated records:", updated_count)

# OUTPUT:
#
# Updated records: 9


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

"""
update() directly updates the database rows
matching the QuerySet.

Here:
    Employee.objects.filter(department_id=1)
means:
    Find all employees belonging to Department 1.

Then:

    .update(salary=70000)

means:

    Set salary = 70000 for all those employees.


Before:

    Test User  -> 50000
    Rahul      -> 50000
    Yogesh     -> 30000
    sachin     -> 40000
    Ishan      -> 70000
    Sanju      -> 6777
    Rahul      -> 50000
    Yogesh     -> 30000
    Sachin     -> 40000


After:

    AB Bhai    -> 70000
    Rahul      -> 70000
    Yogesh     -> 70000
    sachin     -> 70000
    Ishan      -> 70000
    Sanju      -> 70000
    Rahul      -> 70000
    Yogesh     -> 70000
    Sachin     -> 70000


Return:

    Number of rows updated
"""


# ============================================================
# 3. UPDATE_OR_CREATE
#    Using update_or_create()
# ============================================================

print("\n================ 3. UPDATE_OR_CREATE ======")

employee, created = Employee.objects.update_or_create(

    email="test@example.com",

    defaults={
        "name": "Test User Updated",
        "salary": 55000,
        "age": 31,
        "status": "active",
        "department": department,
    }
)

print("Employee:", employee)
print("Created:", created)

# OUTPUT:
#
# Employee: Test User Updated
# Created: False


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

"""
update_or_create() performs two possible operations:

    1. UPDATE
    2. CREATE


It first checks:

    Does email="test@example.com" exist?


CASE 1:
    Record exists

    -> UPDATE existing record

    created = False


CASE 2:
    Record does not exist

    -> CREATE new record

    created = True


In our case:

    test@example.com

already exists for employee ID 3.

Therefore:

    Existing record -> UPDATE

Result:

    Name   = Test User Updated
    Salary = 55000
    Age    = 31

And:

    created = False
"""


# ============================================================
# 4. F() - Database-Side Update
# ============================================================

print("\n================ 4. F() ====================")

employee = Employee.objects.get(id=8)

print("Before:", employee.salary)

Employee.objects.filter(
    id=8
).update(
    salary=F("salary") + 5000
)

employee.refresh_from_db()

print("After :", employee.salary)

# OUTPUT:
#
# Before: 70000.00
# After : 75000.00


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

"""
F() allows us to refer to the existing value of a
database field.

Example:

    salary = F("salary") + 5000


Suppose:

    salary = 70000

Database performs:

    70000 + 5000

Result:

    75000


Without F():

    employee = Employee.objects.get(id=8)

    employee.salary = employee.salary + 5000

    employee.save()


With F():

    Employee.objects.filter(id=8).update(
        salary=F("salary") + 5000
    )


The calculation happens at the DATABASE level.


Common examples:

    salary = F("salary") + 5000

    salary = F("salary") - 2000

    age = F("age") + 1


Very useful for:

    Increment
    Decrement
    Counters
    Database-side calculations
"""


# ============================================================
# 5. BULK_UPDATE - Using bulk_update()
# ============================================================

print("\n================ 5. BULK_UPDATE ===========")

employees = Employee.objects.filter(
    id__in=[10, 11, 12]
)

for emp in employees:

    emp.salary = 80000


Employee.objects.bulk_update(
    employees,
    ["salary"]
)

print("Bulk update completed")

# OUTPUT:
#
# Bulk update completed


# ------------------------------------------------------------
# VERIFY BULK UPDATE
# ------------------------------------------------------------

employees = Employee.objects.filter(
    id__in=[10, 11, 12]
)

for emp in employees:

    print(
        emp.id,
        emp.name,
        emp.salary
    )

# OUTPUT:
#
# 10 Yogesh 80000.00
# 11 sachin 80000.00
# 12 Ishan 80000.00


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

"""
bulk_update() is used when we already have multiple
model objects and want to update them together.

Step 1:
    Get multiple objects

    employees = Employee.objects.filter(
        id__in=[10, 11, 12]
    )


Step 2:
    Change values in Python

    for emp in employees:
        emp.salary = 80000


Step 3:
    Save changes together

    Employee.objects.bulk_update(
        employees,
        ["salary"]
    )


Before:

    10 Yogesh  70000
    11 sachin  70000
    12 Ishan   70000


After:

    10 Yogesh  80000
    11 sachin  80000
    12 Ishan   80000


Main advantage:

    Avoid calling save() separately for every object.

Instead of:

    emp1.save()
    emp2.save()
    emp3.save()

Use:

    bulk_update(...)
"""


# ============================================================
# 6. SAVE(update_fields=...)
# ============================================================

print("\n================ 6. SAVE(update_fields) ====")

employee = Employee.objects.get(id=13)

employee.name = "Sanju Updated"
employee.salary = 85000

employee.save(
    update_fields=[
        "name",
        "salary"
    ]
)

print(
    employee.id,
    employee.name,
    employee.salary
)

# OUTPUT:
#
# 13 Sanju Updated 85000.00


# ------------------------------------------------------------
# EXPLANATION
# ------------------------------------------------------------

"""
save(update_fields=...) tells Django to update
only the specified fields.

Here:

    employee.save(
        update_fields=["name", "salary"]
    )


Only these fields are updated:

    name
    salary


Other fields are not included in the UPDATE.


Useful when:

    Only a few fields have changed
    and you don't want to update every field.
"""


# ============================================================
# FINAL SUMMARY
# ============================================================

"""
==============================================================
DJANGO ORM - UPDATE METHODS
==============================================================

1. save()
--------------------------------------------------------------
employee = Employee.objects.get(id=3)

employee.name = "AB Bhai"
employee.save()

Use:
    Update/save ONE model object.


2. update()
--------------------------------------------------------------
Employee.objects.filter(
    department_id=1
).update(
    salary=70000
)

Use:
    Update ONE or MANY database rows.

Returns:
    Number of rows updated.


3. update_or_create()
--------------------------------------------------------------
Employee.objects.update_or_create(
    email="test@example.com",
    defaults={...}
)

Use:
    UPDATE if exists
    CREATE if not exists.

Returns:
    (object, created)


4. F()
--------------------------------------------------------------
Employee.objects.filter(
    id=8
).update(
    salary=F("salary") + 5000
)

Use:
    Database-side calculation.


5. bulk_update()
--------------------------------------------------------------
Employee.objects.bulk_update(
    employees,
    ["salary"]
)

Use:
    Update multiple existing model objects
    efficiently.


6. save(update_fields=...)
--------------------------------------------------------------
employee.save(
    update_fields=["name", "salary"]
)

Use:
    Update only selected fields.
==============================================================
"""