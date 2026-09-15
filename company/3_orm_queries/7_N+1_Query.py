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
== N+1 is a database performance problem where we make 1 query to fetch the main records and then N additional queries to fetch related data for each record.
== In Django, we can usually solve this using select_related() or prefetch_related().
== One line to remember:
    N+1 = 1 main query + N extra queries.


❌ Without select_related()
employees = Employee.objects.all()
for emp in employees:
    print(emp.name)
    print(emp.department.name)


What happens?
1️⃣ Fetch all Employees
        ↓
   1 query

2️⃣ Access emp.department
        ↓
   Extra query for Department

3️⃣ Repeat for every Employee
        ↓
   N extra queries
Important:- Employee.objects.all() fetches the Employee records, but the related Department data is fetched when we access emp.department.

✅ With select_related()
employees = Employee.objects.select_related("department")

for emp in employees:
    print(emp.name)
    print(emp.department.name)

Employee
    +
Department
    ↓
   JOIN
    ↓
Fetched together ✅

So when we do:

emp.department.name

Django doesn't need another query for that Department.

"""


employee=Employee.objects.all()
# But it has NOT fetched the Department objects yet.
for emp in employee:
    print(emp.name)
    print(emp.department.name) #Here we are makinga another query for department but using select_related() we avoid this department query

employee=Employee.objects.select_related()

for emp in employee:
    print(emp.name)
    print(emp.department.name)

# Q1. Get all employees along with their Department using select_related() and print employee name + department name.

# Q2. Get all employees along with their Department and print:

# Employee name
# Department name
# Department location

# Q3. Get all employees from the Finance department using select_related().

# Q4. Get all employees and print their:

# Name
# Salary
# Department manager

# Q5. Get all employees whose department is located in Pune, using select_related().

# Q6. Explain why this code can cause an N+1 problem:

# employees = Employee.objects.all()

# for emp in employees:
#     print(emp.name)
#     print(emp.department.name)

# Q7. Modify Q6 to avoid the N+1 problem using select_related().

# Q8. 🔥 What is the difference between:

# Employee.objects.all()

# and

# Employee.objects.select_related("department")