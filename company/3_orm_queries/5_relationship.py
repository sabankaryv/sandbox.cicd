# ============================================================
# DJANGO ORM - RELATIONSHIP QUERIES
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
# RELATIONSHIP
# ============================================================
"""
Employee
    |
    | department (ForeignKey)
    ↓
Department
Employee table:
    department_id
Department table:
    id
    name
    location
    manager
    budget
    is_active
"""
# ============================================================
# STEP 1 - EMPLOYEE → DEPARTMENT
# ============================================================
employee = Employee.objects.get(id=3)
print("Employee Name      :", employee.name)
print("Department Name    :", employee.department.name)
print("Department Location:", employee.department.location)
print("Department Manager :", employee.department.manager)
print("Department Budget  :", employee.department.budget)
print("Department Active  :", employee.department.is_active)

employee1=Employee.objects.get(id=8)
print("Employee Name: ",employee1.name)
print("Department Name: ",employee1.department.name)
print("Department Location: ",employee1.department.location)
print("Department Budget: ",employee1.department.budget)
# ============================================================
# EXPLANATION
# ============================================================
"""
employee
    ↓
Employee object
employee.department
    ↓
Department object
employee.department.name
    ↓
Department name


employee.department.location
    ↓
Department location


employee.department.manager
    ↓
Department manager


employee.department.budget
    ↓
Department budget


employee.department.is_active
    ↓
Department active status


IMPORTANT:

Employee table does NOT contain:

    department_name
    department_location
    department_manager
    department_budget


Employee contains:

    department_id


Because department is a ForeignKey:

    Employee.department
            ↓
       Department object


So we can access fields of the related Department:

    employee.department.name
    employee.department.location
    employee.department.manager
    employee.department.budget
    employee.department.is_active
"""
# ============================================================
# OUTPUT
# ============================================================
"""
OUTPUT:
Employee Name      : AB Bhai
Department Name    : Finance
Department Location: Pune
Department Manager : Amit
Department Budget  : 5000000.00
Department Active  : True
"""


# ============================================================
# STEP 2 - REVERSE RELATIONSHIP
# Department → Employees
# ============================================================
# ============================================================
# QUESTION 1
# ============================================================

"""
Q1. Get all employees who belong to the Finance department.
"""
employee=Employee.objects.filter(department__id=1)
for emp in employee:
    print(emp.name)


# above query is forward relation but if asked reverse relation then

department=Department.objects.get(id=1)
employee=department.employee_set.all()
for emp in employee:
    print(emp.name)
# ============================================================
# STEP 1 - FORWARD RELATIONSHIP
# Employee → Department
# ============================================================


# ============================================================
# QUESTION 1
# ============================================================

"""
Q1. Get the department of employee with ID 3.
"""

employee = Employee.objects.get(id=3)

department = employee.department

print(department)


# OUTPUT:
#
# Finance


# ============================================================
# QUESTION 2
# ============================================================

"""
Q2. Get the department name of employee with ID 3.
"""

employee = Employee.objects.get(id=3)

print(employee.department.name)


# OUTPUT:
#
# Finance


# ============================================================
# QUESTION 3
# ============================================================

"""
Q3. Get the department location of employee with ID 3.
"""

employee = Employee.objects.get(id=3)

print(employee.department.location)


# OUTPUT:
#
# Pune


# ============================================================
# QUESTION 4
# ============================================================

"""
Q4. Get the department manager of employee with ID 3.
"""

employee = Employee.objects.get(id=3)

print(employee.department.manager)


# OUTPUT:
#
# Amit


# ============================================================
# QUESTION 5
# ============================================================

"""
Q5. Get the department budget of employee with ID 3.
"""

employee = Employee.objects.get(id=3)

print(employee.department.budget)


# OUTPUT:
#
# 5000000.00


# ============================================================
# QUESTION 6
# ============================================================

"""
Q6. Get the department active status of employee with ID 3.
"""

employee = Employee.objects.get(id=3)

print(employee.department.is_active)


# OUTPUT:
#
# True


# ============================================================
# QUESTION 7
# ============================================================

"""
Q7. Print employee name along with department name.
"""

employee = Employee.objects.get(id=3)

print(
    employee.name,
    employee.department.name
)


# OUTPUT:
#
# AB Bhai Finance


# ============================================================
# QUESTION 8
# ============================================================

"""
Q8. Print employee name, department name and location.
"""

employee = Employee.objects.get(id=3)

print(
    employee.name,
    employee.department.name,
    employee.department.location
)


# OUTPUT:
#
# AB Bhai Finance Pune


# ============================================================
# QUESTION 9
# ============================================================

"""
Q9. Get employee ID 3's department object and
    print all important department details.
"""

employee = Employee.objects.get(id=3)

department = employee.department

print("Department Name :", department.name)
print("Location        :", department.location)
print("Manager         :", department.manager)
print("Budget          :", department.budget)
print("Active          :", department.is_active)


# OUTPUT:
#
# Department Name : Finance
# Location        : Pune
# Manager         : Amit
# Budget          : 5000000.00
# Active          : True

# ============================================================
# QUESTION 2
# ============================================================

"""
Q2. Get the total number of employees in the Finance department.
"""

employee=Employee.objects.filter(department__id=1).count()
print(employee)
# above query is forward relation but if asked reverse relation then
department=Department.objects.get(id=1)
employee=department.employee_set.all().count()
print("=====>",employee)

# ============================================================
# QUESTION 3
# ============================================================

"""
Q3. Check whether the Finance department has any employees.
"""
employee=Employee.objects.filter(department__id=1).exists()
print(employee)
# above query is forward relation but if asked reverse relation then
department=Department.objects.get(id=1)
employee=department.employee_set.exists()
print(employee)


# ============================================================
# QUESTION 4
# ============================================================

"""
Q4. Get the first employee belonging to the Finance department.
"""
employee=Employee.objects.filter(department__id=1).first()
print(employee)
# above query is forward relation but if asked reverse relation then

# 1. Get all employees of a department.
# 2. Count employees in a department.
# 3. Check whether a department has employees.
# 4. Get the first employee of a department.
# 5. Get the last employee of a department.
# 6. Get employees with salary > X in a department.
# 7. Get employees with age > X in a department.
# 8. Get only employee names of a department.
# 9. Exclude resigned employees from a department.
# 10. Get active employees belonging to a department.



# ============================================================
# STEP 3 - RELATIONSHIP FILTERING
# Employee → Department
# ============================================================

"""
IMPORTANT:

When filtering through a ForeignKey relationship,
we use double underscore:

    __

Example:

    department__name

Meaning:

    Employee
        ↓
    Department
        ↓
    name
"""


# ============================================================
# QUESTION 1
# ============================================================

"""
Q1. Get all employees who belong to the Finance department.
"""

employees = Employee.objects.filter(
    department__name="Finance"
)

for emp in employees:
    print(emp.name)


# OUTPUT:
#
# AB Bhai
# Rahul
# Yogesh
# sachin
# Ishan
# Sanju
# Rahul
# Yogesh
# Sachin


# ============================================================
# EXPLANATION
# ============================================================

"""
department__name means:

Employee
    ↓
department
    ↓
Department
    ↓
name

So:

department__name="Finance"

means:

"Find employees whose department name is Finance."
"""


# ============================================================
# QUESTION 2
# ============================================================

"""
Q2. Get all employees whose department is located in Pune.
"""

employees = Employee.objects.filter(
    department__location="Pune"
)

for emp in employees:
    print(
        emp.name,
        emp.department.name
    )


# OUTPUT:
#
# AB Bhai Finance
# Rahul Finance
# Yogesh Finance
# sachin Finance
# Ishan Finance
# Sanju Finance
# Rahul Finance
# Yogesh Finance
# Sachin Finance


# ============================================================
# EXPLANATION
# ============================================================

"""
department__location means:

Employee
    ↓
Department
    ↓
location

Find employees where:

Department.location == "Pune"
"""


# ============================================================
# QUESTION 3
# ============================================================

"""
Q3. Get all employees who belong to a department
    having a budget greater than 50 lakh.
"""

employees = Employee.objects.filter(
    department__budget__gt=5000000
)

for emp in employees:
    print(
        emp.name,
        emp.department.name,
        emp.department.budget
    )


# OUTPUT:
#
# AB Bhai Finance 5000000.00
# Rahul Finance 5000000.00
# ...
#
# NOTE:
# With budget exactly 5000000, these records will NOT match
# because __gt means greater than.
"""


# ============================================================
# EXPLANATION
# ============================================================

"""


# ============================================================
# QUESTION 4
# ============================================================

"""
Q4. Get all employees whose department is active.
"""

employees = Employee.objects.filter(
    department__is_active=True
)

for emp in employees:
    print(emp.name)


# OUTPUT:
#
# AB Bhai
# Rahul
# Yogesh
# sachin
# Ishan
# Sanju
# Rahul
# Yogesh
# Sachin


# ============================================================
# EXPLANATION
# ============================================================

"""
department__is_active

means:

Employee
    ↓
Department
    ↓
is_active

Find employees whose department is active.
"""


# ============================================================
# QUESTION 5
# ============================================================

"""
Q5. Get all employees whose department manager is Amit.
"""

employees = Employee.objects.filter(
    department__manager="Amit"
)

for emp in employees:
    print(
        emp.name,
        emp.department.manager
    )


# OUTPUT:
#
# AB Bhai Amit
# Rahul Amit
# Yogesh Amit
# sachin Amit
# Ishan Amit
# Sanju Amit
# Rahul Amit
# Yogesh Amit
# Sachin Amit


# ============================================================
# EXPLANATION
# ============================================================

"""
department__manager

means:

Employee
    ↓
Department
    ↓
manager

Find employees whose department manager is Amit.
"""


# ============================================================
# QUESTION 6
# ============================================================

"""
Q6. Get employees belonging to Finance department
    and having salary greater than 50000.
"""

employees = Employee.objects.filter(
    department__name="Finance",
    salary__gt=50000
)

for emp in employees:
    print(
        emp.name,
        emp.salary,
        emp.department.name
    )


# OUTPUT:
#
# Rahul 75000.00 Finance
# Yogesh 80000.00 Finance
# sachin 80000.00 Finance
# Ishan 80000.00 Finance
# ...


# ============================================================
# EXPLANATION
# ============================================================

"""
Here we are filtering using:

1. Related Department field

    department__name="Finance"

2. Employee's own field

    salary__gt=50000

So:

Employee
   |
   +---- salary > 50000
   |
   └---- Department
             |
             └---- name = Finance
"""


# ============================================================
# QUESTION 7
# ============================================================

"""
Q7. Get employees whose department is NOT Finance.
"""

employees = Employee.objects.exclude(
    department__name="Finance"
)

for emp in employees:
    print(emp.name)


# OUTPUT:
#
# Employees belonging to departments other than Finance
#
# If all your current employees are in Finance:
#
# <no output>

# ============================================================
# STEP 4 - MULTIPLE CONDITION QUERIES
# ============================================================

"""
We can combine:

Employee fields
        +
Department fields

Example:

Employee salary > 50000
AND
Department name = Finance
"""


# ============================================================
# QUESTION 1
# ============================================================

"""
Q1. Get employees who belong to the Finance department
    AND have salary greater than 50000.
"""
employees = Employee.objects.filter(department__name="Finance",salary__gt=50000)
print("\n" + "=" * 70)
print("        EMPLOYEES WITH SALARY > 50,000")
print("=" * 70)

for emp in employees:
    print(f"""
Employee   : {emp.name}
Salary     : ₹{emp.salary:,.2f}
Department : {emp.department.name}
Budget     : ₹{emp.department.budget:,.2f}
Manager    : {emp.department.manager}
{'-' * 70}""")


# ============================================================
# QUESTION 2
# ============================================================
"""
Q2. Get employees who are older than 25
    AND belong to the Finance department.
"""
employees=Employee.objects.filter(department__id=1,age__gt=25)
print("\n" + "=" * 70)
print("        EMPLOYEES WITH AGE > 25")
print("=" * 70)

for emp in employees:
    print(f"""
Employee   : {emp.name}
Salary     : ₹{emp.salary:,.2f}
Department : {emp.department.name}
Budget     : ₹{emp.department.budget:,.2f}
Manager    : {emp.department.manager}
{'-' * 70}""")
# ============================================================
# QUESTION 3
# ============================================================
"""
Q3. Get employees who belong to Finance
    AND whose department is located in Pune.
"""
employees=Employee.objects.filter(department__id=1,department__location="pune")
print("\n" + "=" * 70)
print("        EMPLOYEES WITH LOCATION PUNE")
print("=" * 70)

for emp in employees:
    print(f"""
Employee   : {emp.name}
Salary     : ₹{emp.salary:,.2f}
Department : {emp.department.name}
Budget     : ₹{emp.department.budget:,.2f}
Manager    : {emp.department.manager}
{'-' * 70}""")

# ============================================================
# QUESTION 4
# ============================================================
"""
Q4. Get employees whose salary is greater than 50000
    AND whose department is active.
"""

employees=Employee.objects.filter(salary__gt=50000,status="active")
print("\n" + "=" * 70)
print("        EMPLOYEES WITH DEPARTMENT ACTIVE")
print("=" * 70)
for emp in employees:
    print(f"""
Employee   : {emp.name}
Salary     : ₹{emp.salary:,.2f}
Department : {emp.department.name}
Budget     : ₹{emp.department.budget:,.2f}
Manager    : {emp.department.manager}
{'-' * 70}""")

# ============================================================
# QUESTION 5
# ============================================================

"""
Q5. Get employees who are older than 25
    AND belong to a department whose budget
    is greater than 5000000.
"""

employees = Employee.objects.filter(
    age__gt=25,
    department__budget__gt=5000000
)

for emp in employees:
    print(
        emp.name,
        emp.age,
        emp.department.name,
        emp.department.budget
    )


# OUTPUT:
#
# Depends on your Department budget.
#
# If Finance budget = 5000000 exactly,
# Finance employees will NOT appear because:
#
# 5000000 > 5000000
#        ❌
# ============================================================
# QUESTION 6
# ============================================================

"""
Q6. Get employees who have salary greater than 50000
    AND age greater than 25
    AND belong to Finance.
"""

employees = Employee.objects.filter(
    salary__gt=50000,
    age__gt=25,
    department__name="Finance"
)

for emp in employees:
    print(
        emp.name,
        emp.salary,
        emp.age,
        emp.department.name
    )


# OUTPUT:
#
# Rahul 75000.00 25 Finance
#
# Rahul will NOT appear because:
#
# age > 25
#
# 25 > 25
#    ❌
#
# Other matching employees will appear.
# ============================================================
# QUESTION 7
# ============================================================

"""
Q7. Get employees from Pune departments
    AND salary greater than 50000
    AND status is active.
"""

employees = Employee.objects.filter(
    department__location="Pune",
    salary__gt=50000,
    status="active"
)

for emp in employees:
    print(
        emp.name,
        emp.salary,
        emp.status,
        emp.department.location
    )


# OUTPUT:
#
# Rahul 75000.00 active Pune
# Yogesh 80000.00 active Pune



