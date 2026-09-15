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
# 1.=
# ============================================================

employee=Employee.objects.filter(age=30)
for emp in employee:
    print(emp.name)
    print(emp.id)

# ============================================================
# 2.gt
# ============================================================
