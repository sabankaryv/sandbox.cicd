# ============================================================
# DJANGO ORM - Q OBJECTS
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
from django.db.models import Q

"""
== Q objects are used in Django ORM to build complex query conditions using AND, OR, and NOT logic.
== 

|  → OR
&  → AND
~  → NOT


"""
# ============================================================
# QUESTION 1
# ============================================================
"""
Q1. Get all employees whose:
    salary > 50000
    OR
    age > 30
"""
# ============================================================
# ANSWER
# ============================================================
employees = Employee.objects.filter(Q(salary__gt=50000)|Q(age__gt=30))
# ============================================================
# OUTPUT
# ============================================================
for emp in employees:
    print(
        "Name:", emp.name,
        "| Salary:", emp.salary,
        "| Age:", emp.age
    )
# Q1
# Get all employees whose salary is greater than 50,000 OR age is greater than 30.
# Q2
# Get all employees who belong to Finance OR IT department.
# Q3
# Get all employees whose salary is greater than 50,000 AND age is greater than 30 using Q().
# Q4
# Get all employees who do NOT belong to Finance department.

# Q5

# Get employees who are from Finance OR have salary greater than 70,000.

# Q6

# Get employees from Finance AND (salary > 50,000 OR age > 30).

# Q7

# Get employees whose age is less than 25 OR salary is greater than 80,000.

# Q8

# Get employees who are NOT from Finance OR salary is greater than 70,000.

# Q9

# Get employees who belong to Finance OR Pune department location.

# Q10 🔥

# Get employees who satisfy:

# (Finance OR IT) AND salary > 50,000