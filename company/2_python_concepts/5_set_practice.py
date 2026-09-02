# ============================================================
# 5_set_practice.py
# SET PRACTICE - Python + API + Battle Preparation
# ============================================================


# ============================================================
# 1. CREATE SET
# ============================================================

numbers = {1, 2, 3, 4}

print(numbers)


# Empty set

numbers = set()

print(type(numbers))


# ============================================================
# 2. DUPLICATES AUTOMATICALLY REMOVED
# ============================================================

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)


# ============================================================
# 3. ADD
# ============================================================

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)


# ============================================================
# 4. UPDATE
# ============================================================

numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)


# ============================================================
# 5. REMOVE
# ============================================================

numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)


# ============================================================
# 6. DISCARD
# Does not raise error if missing
# ============================================================

numbers = {1, 2, 3}

numbers.discard(10)

print(numbers)


# ============================================================
# 7. POP
# ============================================================

numbers = {1, 2, 3}

value = numbers.pop()

print(value)
print(numbers)


# ============================================================
# 8. CLEAR
# ============================================================

numbers = {1, 2, 3}

numbers.clear()

print(numbers)


# ============================================================
# 9. MEMBERSHIP
# Very important
# ============================================================

numbers = {10, 20, 30}

print(20 in numbers)
print(100 in numbers)


# ============================================================
# 10. UNION
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a.union(b))


# ============================================================
# 11. INTERSECTION
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
print(a.intersection(b))


# ============================================================
# 12. DIFFERENCE
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
print(a.difference(b))


# ============================================================
# 13. SYMMETRIC DIFFERENCE
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)


# ============================================================
# 14. SUBSET
# ============================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))


# ============================================================
# 15. SUPERSET
# ============================================================

a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))


# ============================================================
# 16. DISJOINT
# ============================================================

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))


# ============================================================
# 17. LIST -> SET
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

unique = set(numbers)

print(unique)


# ============================================================
# 18. SET -> LIST
# ============================================================

numbers = {1, 2, 3}

result = list(numbers)

print(result)


# ============================================================
# 19. REMOVE DUPLICATES PRESERVING ORDER
# ============================================================

numbers = [1, 2, 2, 3, 1, 4]

result = list(dict.fromkeys(numbers))

print(result)


# ============================================================
# 20. FIND DUPLICATES
# ============================================================

numbers = [1, 2, 3, 2, 4, 1]

seen = set()
duplicates = set()

for number in numbers:

    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print(duplicates)


# ============================================================
# 21. COMMON ELEMENTS
# API / DATA PROCESSING
# ============================================================

old_users = {1, 2, 3, 4}
new_users = {3, 4, 5, 6}

common = old_users & new_users

print(common)


# ============================================================
# 22. NEW USERS
# ============================================================

new_users = {3, 4, 5, 6}
old_users = {1, 2, 3, 4}

result = new_users - old_users

print(result)


# ============================================================
# 23. MISSING IDs
# ============================================================

expected_ids = {1, 2, 3, 4, 5}
received_ids = {1, 2, 4}

missing = expected_ids - received_ids

print(missing)


# ============================================================
# 24. EXTRA IDs
# ============================================================

expected_ids = {1, 2, 3}
received_ids = {1, 2, 3, 4, 5}

extra = received_ids - expected_ids

print(extra)


# ============================================================
# 25. API VALIDATION
# ============================================================

required_fields = {"id", "name", "email"}

received_fields = {"id", "name"}

missing = required_fields - received_fields

print(missing)


# ============================================================
# 26. PERMISSION CHECK
# ============================================================

required_permissions = {
    "read",
    "write"
}

user_permissions = {
    "read",
    "write",
    "delete"
}

if required_permissions.issubset(user_permissions):
    print("Allowed")
else:
    print("Denied")


# ============================================================
# 27. UNIQUE USER IDS FROM API DATA
# ============================================================

users = [
    {"id": 101, "name": "John"},
    {"id": 102, "name": "Alex"},
    {"id": 101, "name": "John"},
]

user_ids = {user["id"] for user in users}

print(user_ids)


# ============================================================
# 28. SET COMPREHENSION
# ============================================================

numbers = [1, 2, 2, 3, 3, 4]

result = {x * 2 for x in numbers}

print(result)

# 1. Why does set remove duplicates?
#
# 2. Why is set membership faster than list membership generally?
#
# 3. Difference between remove() and discard()?
#
# 4. Difference between union and intersection?
#
# 5. How to find common elements?
#
# 6. How to find missing IDs?
#
# 7. How to find duplicate values?
#
# 8. How to remove duplicates from a list?
#
# 9. How to preserve order while removing duplicates?
#
# 10. What is a frozenset?
#
# 11. Can a list be an element of a set?
#
# 12. Can a tuple be an element of a set?