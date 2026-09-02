# ============================================================
# 6_dict_practice.py
# DICTIONARY PRACTICE - Python + API + Battle Preparation
# ============================================================


# ============================================================
# 1. CREATE DICTIONARY
# ============================================================

user = {
    "id": 101,
    "name": "John",
    "age": 30
}

print(user)


# ============================================================
# 2. ACCESS VALUES
# ============================================================

print(user["name"])
print(user["age"])


# ============================================================
# 3. GET()
# Safer API handling
# ============================================================

print(user.get("name"))
print(user.get("email"))

print(user.get("email", "Not Available"))


# ============================================================
# 4. ADD KEY
# ============================================================

user["email"] = "john@test.com"

print(user)


# ============================================================
# 5. UPDATE VALUE
# ============================================================

user["age"] = 31

print(user)


# ============================================================
# 6. UPDATE MULTIPLE VALUES
# ============================================================

user.update({
    "age": 32,
    "city": "Pune"
})

print(user)


# ============================================================
# 7. DELETE
# ============================================================

user.pop("city")

print(user)


# ============================================================
# 8. POP WITH DEFAULT
# ============================================================

value = user.pop("address", None)

print(value)


# ============================================================
# 9. KEYS
# ============================================================

print(user.keys())


# ============================================================
# 10. VALUES
# ============================================================

print(user.values())


# ============================================================
# 11. ITEMS
# ============================================================

print(user.items())


# ============================================================
# 12. LOOP KEYS
# ============================================================

for key in user:
    print(key)


# ============================================================
# 13. LOOP VALUES
# ============================================================

for value in user.values():
    print(value)


# ============================================================
# 14. LOOP KEY + VALUE
# ============================================================

for key, value in user.items():
    print(key, value)


# ============================================================
# 15. CHECK KEY
# ============================================================

if "name" in user:
    print("Name exists")


# ============================================================
# 16. CHECK VALUE
# ============================================================

if "John" in user.values():
    print("John exists")


# ============================================================
# 17. EMPTY DICTIONARY
# ============================================================

data = {}

print(data)


# ============================================================
# 18. DICTIONARY COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4]

result = {
    x: x * x
    for x in numbers
}

print(result)


# ============================================================
# 19. DICT FROM TWO LISTS
# ============================================================

keys = ["name", "age", "city"]
values = ["John", 30, "Pune"]

result = dict(zip(keys, values))

print(result)


# ============================================================
# 20. NESTED DICTIONARY
# ============================================================

user = {
    "id": 101,
    "name": "John",
    "address": {
        "city": "Pune",
        "pincode": 411001
    }
}

print(user["address"]["city"])


# ============================================================
# 21. SAFE NESTED ACCESS
# ============================================================

city = user.get("address", {}).get("city")

print(city)


# ============================================================
# 22. LIST OF DICTS
# MOST IMPORTANT FOR APIs
# ============================================================

users = [
    {"id": 1, "name": "John", "salary": 50000},
    {"id": 2, "name": "Alex", "salary": 70000},
    {"id": 3, "name": "Mike", "salary": 60000}
]

print(users)


# ============================================================
# 23. GET ALL NAMES
# ============================================================

names = [
    user.get("name")
    for user in users
]

print(names)


# ============================================================
# 24. FILTER USERS
# ============================================================

result = [
    user
    for user in users
    if user.get("salary", 0) > 55000
]

print(result)


# ============================================================
# 25. FIND USER BY ID
# ============================================================

user_id = 2

result = next(
    (
        user
        for user in users
        if user.get("id") == user_id
    ),
    None
)

print(result)


# ============================================================
# 26. FIND ALL USERS BY CONDITION
# ============================================================

result = [
    user
    for user in users
    if user.get("salary", 0) >= 60000
]

print(result)


# ============================================================
# 27. SORT DICTIONARY DATA
# ============================================================

result = sorted(
    users,
    key=lambda x: x.get("salary", 0)
)

print(result)


# ============================================================
# 28. SORT DESCENDING
# ============================================================

result = sorted(
    users,
    key=lambda x: x.get("salary", 0),
    reverse=True
)

print(result)


# ============================================================
# 29. MAX RECORD
# ============================================================

result = max(
    users,
    key=lambda x: x.get("salary", 0)
)

print(result)


# ============================================================
# 30. MIN RECORD
# ============================================================

result = min(
    users,
    key=lambda x: x.get("salary", 0)
)

print(result)


# ============================================================
# 31. COUNT FREQUENCY
# ============================================================

numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for number in numbers:

    frequency[number] = (
        frequency.get(number, 0) + 1
    )

print(frequency)


# ============================================================
# 32. GROUP DATA
# VERY IMPORTANT
# ============================================================

users = [
    {"name": "John", "department": "IT"},
    {"name": "Alex", "department": "HR"},
    {"name": "Mike", "department": "IT"},
]

grouped = {}

for user in users:

    department = user["department"]

    grouped.setdefault(
        department,
        []
    ).append(user)

print(grouped)


# ============================================================
# 33. GROUP USING defaultdict
# ============================================================

from collections import defaultdict

grouped = defaultdict(list)

for user in users:

    grouped[user["department"]].append(user)

print(dict(grouped))


# ============================================================
# 34. DICTIONARY WITH TUPLE KEY
# Important API / counting pattern
# ============================================================

data = {}

requests = [
    {"user_id": 101, "endpoint": "/orders"},
    {"user_id": 102, "endpoint": "/users"},
    {"user_id": 101, "endpoint": "/orders"},
    {"user_id": 103, "endpoint": "/orders"},
    {"user_id": 102, "endpoint": "/users"},
    {"user_id": 101, "endpoint": "/payments"},
]

for request in requests:

    key = (
        request["user_id"],
        request["endpoint"]
    )

    data[key] = data.get(key, 0) + 1

print(data)


# ============================================================
# 35. SAME USING Counter
# ============================================================

from collections import Counter

result = Counter(
    (
        request["user_id"],
        request["endpoint"]
    )
    for request in requests
)

print(result)


# ============================================================
# 36. CONVERT LIST TO DICT BY ID
# VERY COMMON API PATTERN
# ============================================================

users = [
    {"id": 101, "name": "John"},
    {"id": 102, "name": "Alex"},
    {"id": 103, "name": "Mike"}
]

user_dict = {
    user["id"]: user
    for user in users
}

print(user_dict)


# ============================================================
# 37. MERGE DICTIONARIES
# ============================================================

a = {
    "name": "John",
    "age": 30
}

b = {
    "city": "Pune",
    "salary": 50000
}

result = {**a, **b}

print(result)


# Python 3.9+

result = a | b

print(result)


# ============================================================
# 38. DICT COPY
# ============================================================

user = {
    "name": "John",
    "age": 30
}

copy_user = user.copy()

print(copy_user)


# ============================================================
# 39. SHALLOW COPY
# ============================================================

user = {
    "name": "John",
    "address": {
        "city": "Pune"
    }
}

copy_user = user.copy()

copy_user["address"]["city"] = "Mumbai"

print(user)
print(copy_user)


# ============================================================
# 40. DEEP COPY
# ============================================================

import copy

user = {
    "name": "John",
    "address": {
        "city": "Pune"
    }
}

copy_user = copy.deepcopy(user)

copy_user["address"]["city"] = "Mumbai"

print(user)
print(copy_user)


# ============================================================
# 41. API RESPONSE
# ============================================================

response = {
    "status": True,
    "message": "Users fetched successfully",
    "data": [
        {
            "id": 1,
            "name": "John"
        },
        {
            "id": 2,
            "name": "Alex"
        }
    ]
}

users = response.get("data", [])

print(users)


# ============================================================
# 42. HANDLE MISSING / NONE DATA
# ============================================================

response = {
    "status": True,
    "data": None
}

users = response.get("data") or []

print(users)


# ============================================================
# 43. REMOVE KEYS
# ============================================================

user = {
    "id": 101,
    "name": "John",
    "password": "secret",
    "token": "abc"
}

user.pop("password", None)
user.pop("token", None)

print(user)


# ============================================================
# 44. CREATE API RESPONSE
# ============================================================

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alex"}
]

response = {
    "status": True,
    "count": len(users),
    "data": users
}

print(response)

# ============================================================
# DICTIONARY BATTLE QUESTIONS
# ============================================================

# 1. Count frequency of characters in a string.
#
# 2. Count frequency of numbers in a list.
#
# 3. Find duplicate values.
#
# 4. Find the first non-repeating character.
#
# 5. Find the key having maximum value.
#
# 6. Sort dictionary by value.
#
# 7. Sort dictionary by key.
#
# 8. Merge two dictionaries.
#
# 9. Convert two lists into dictionary.
#
# 10. Invert a dictionary.
#
# 11. Group list of dictionaries by a field.
#
# 12. Convert list of dictionaries into dictionary by ID.
#
# 13. Find maximum salary from users.
#
# 14. Find second-highest salary.
#
# 15. Find users belonging to a particular department.
#
# 16. Count users department-wise.
#
# 17. Find duplicate IDs from API response.
#
# 18. Compare two API responses.
#
# 19. Find missing fields from API payload.
#
# 20. Safely access nested dictionary.
#
# 21. Remove sensitive keys from API response.
#
# 22. Flatten nested dictionary.
#
# 23. Merge nested API data.
#
# 24. Build an API response dictionary.
#
# 25. Convert dictionary data into JSON.
#
# 26. Handle None/missing keys.
#
# 27. Difference between [] and .get().
#
# 28. Difference between copy() and deepcopy().
#
# 29. Why can tuple be a dict key but list cannot?
#
# 30. Explain dictionary hashing.