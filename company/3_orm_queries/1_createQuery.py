# 1_createQuery.py

from employee.models import Employee


# ============================================================
# 1. CREATE - Basic
# ============================================================

employee = Employee.objects.create(name="Rahul",age=25,salary=50000)
print(employee)
# ============================================================
# 2. CREATE using save()
# ============================================================

employee = Employee(
    name="Amit",
    age=28,
    salary=60000
)

employee.save()


# ============================================================
# 3. CREATE using create()
# ============================================================

employee = Employee.objects.create(
    name="Sneha",
    age=27,
    salary=55000
)


# ============================================================
# 4. CREATE multiple records - bulk_create()
# ============================================================

employees = [
    Employee(name="Raj", age=30, salary=70000),
    Employee(name="Priya", age=26, salary=52000),
    Employee(name="Vijay", age=32, salary=80000),
]

Employee.objects.bulk_create(employees)


# ============================================================
# 5. bulk_create() with many records
# ============================================================

employees = []

for i in range(10):
    employees.append(
        Employee(
            name=f"Employee {i}",
            age=20 + i,
            salary=30000 + (i * 1000)
        )
    )

Employee.objects.bulk_create(employees)


# ============================================================
# 6. CREATE with ForeignKey
# ============================================================

# Example:
# employee.department = department

employee = Employee.objects.create(
    name="Kiran",
    age=29,
    salary=65000,
    department=department
)


# ============================================================
# 7. CREATE using department_id
# ============================================================

employee = Employee.objects.create(
    name="Suresh",
    age=31,
    salary=72000,
    department_id=1
)


# ============================================================
# 8. CREATE with only required fields
# ============================================================

employee = Employee.objects.create(
    name="Neha"
)


# ============================================================
# 9. CREATE and get returned object
# ============================================================

employee = Employee.objects.create(
    name="Pooja",
    age=24,
    salary=45000
)

print(employee.id)
print(employee.name)
print(employee.salary)


# ============================================================
# 10. CREATE inside transaction
# ============================================================

from django.db import transaction

with transaction.atomic():

    Employee.objects.create(
        name="Employee A",
        age=25,
        salary=50000
    )

    Employee.objects.create(
        name="Employee B",
        age=26,
        salary=55000
    )


# ============================================================
# 11. CREATE using get_or_create()
# ============================================================

employee, created = Employee.objects.get_or_create(
    name="Rahul",
    defaults={
        "age": 25,
        "salary": 50000
    }
)

print(employee)
print(created)


# ============================================================
# 12. CREATE using update_or_create()
# ============================================================

employee, created = Employee.objects.update_or_create(
    name="Rahul",
    defaults={
        "age": 26,
        "salary": 60000
    }
)

print(employee)
print(created)