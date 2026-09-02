# ============================================================
# 3_list_practice.py
# LIST PRACTICE - Python + API + Battle Preparation
# ============================================================


# ============================================================
# 1. BASIC LIST OPERATIONS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])


# ============================================================
# 2. ADD ELEMENTS
# ============================================================

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

numbers.insert(1, 15)
print(numbers)

numbers.extend([50, 60])
print(numbers)


# ============================================================
# 3. REMOVE ELEMENTS
# ============================================================

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)       # remove first occurrence
print(numbers)

value = numbers.pop()    # remove last
print(value)
print(numbers)

numbers.pop(1)           # remove by index
print(numbers)


# ============================================================
# 4. SEARCH / CHECK
# ============================================================

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(100 in numbers)

print(numbers.index(30))
print(numbers.count(20))


# ============================================================
# 5. LOOP THROUGH LIST
# ============================================================

users = ["John", "Alex", "Mike"]

for user in users:
    print(user)


# ============================================================
# 6. ENUMERATE
# ============================================================

for index, user in enumerate(users):
    print(index, user)


# ============================================================
# 7. LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)


# ============================================================
# 8. LIST COMPREHENSION WITH CONDITION
# ============================================================

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)


# ============================================================
# 9. IF / ELSE IN LIST COMPREHENSION
# ============================================================

result = [
    "Even" if x % 2 == 0 else "Odd"
    for x in numbers
]

print(result)


# ============================================================
# 10. FILTER LIST
# ============================================================

numbers = [10, 15, 20, 25, 30]

result = [x for x in numbers if x > 20]

print(result)


# ============================================================
# 11. REMOVE DUPLICATES
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique = list(set(numbers))

print(unique)


# Preserve original order

unique = list(dict.fromkeys(numbers))

print(unique)


# ============================================================
# 12. SORTING
# ============================================================

numbers = [50, 10, 30, 20, 40]

numbers.sort()

print(numbers)


numbers.sort(reverse=True)

print(numbers)


# sorted() returns a new list

numbers = [50, 10, 30, 20, 40]

result = sorted(numbers)

print(result)
print(numbers)


# ============================================================
# 13. MIN / MAX / SUM
# ============================================================

numbers = [10, 20, 30, 40]

print(min(numbers))
print(max(numbers))
print(sum(numbers))


# ============================================================
# 14. REVERSE
# ============================================================

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


# ============================================================
# 15. ZIP TWO LISTS
# ============================================================

names = ["John", "Alex", "Mike"]
ages = [25, 30, 28]

result = list(zip(names, ages))

print(result)


# ============================================================
# 16. ZIP MULTIPLE LISTS
# ============================================================

names = ["John", "Alex", "Mike"]
ages = [25, 30, 28]
cities = ["Pune", "Mumbai", "Delhi"]

result = list(zip(names, ages, cities))

print(result)


# ============================================================
# 17. UNPACKING LIST
# ============================================================

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)


# ============================================================
# 18. STAR UNPACKING
# ============================================================

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)


# ============================================================
# 19. LIST OF DICTIONARIES
# Very important for APIs
# ============================================================

users = [
    {"id": 1, "name": "John", "age": 25},
    {"id": 2, "name": "Alex", "age": 30},
    {"id": 3, "name": "Mike", "age": 28},
]

for user in users:
    print(user["name"])


# ============================================================
# 20. GET ONE FIELD FROM LIST OF DICTS
# ============================================================

names = [user["name"] for user in users]

print(names)


# ============================================================
# 21. FILTER LIST OF DICTS
# ============================================================

result = [
    user
    for user in users
    if user["age"] > 25
]

print(result)


# ============================================================
# 22. SORT LIST OF DICTS
# ============================================================

result = sorted(
    users,
    key=lambda x: x["age"]
)

print(result)


# Descending

result = sorted(
    users,
    key=lambda x: x["age"],
    reverse=True
)

print(result)


# ============================================================
# 23. GET MAX/MIN FROM LIST OF DICTS
# ============================================================

oldest = max(users, key=lambda x: x["age"])

print(oldest)


youngest = min(users, key=lambda x: x["age"])

print(youngest)


# ============================================================
# 24. HANDLE MISSING KEY
# Very important in APIs
# ============================================================

users = [
    {"id": 1, "name": "John"},
    {"id": 2},
    {"id": 3, "name": "Mike"},
]

for user in users:
    print(user.get("name"))


# ============================================================
# 25. DEFAULT VALUE
# ============================================================

for user in users:
    print(user.get("name", "Unknown"))


# ============================================================
# 26. CHECK EMPTY LIST
# ============================================================

users = []

if not users:
    print("No users found")


# ============================================================
# 27. LIST WITH NONE
# ============================================================

data = [10, None, 20, None, 30]

result = [x for x in data if x is not None]

print(result)


# ============================================================
# 28. LIST WITH STRING DATA
# ============================================================

names = ["John", "Alex", "Mike"]

result = [name.upper() for name in names]

print(result)


# ============================================================
# 29. STRING -> LIST
# ============================================================

text = "apple,banana,orange"

result = text.split(",")

print(result)


# ============================================================
# 30. LIST -> STRING
# ============================================================

names = ["John", "Alex", "Mike"]

result = ",".join(names)

print(result)


# ============================================================
# 31. NESTED LIST
# ============================================================

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[0])
print(numbers[1][2])


# ============================================================
# 32. FLATTEN NESTED LIST
# ============================================================

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    number
    for row in numbers
    for number in row
]

print(result)


# ============================================================
# 33. LIST OF LIST OF DICTS
# API STYLE
# ============================================================

data = [
    [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alex"}
    ],
    [
        {"id": 3, "name": "Mike"}
    ]
]

for group in data:
    for user in group:
        print(user["name"])


# ============================================================
# 34. GROUP DATA
# ============================================================

users = [
    {"name": "John", "department": "IT"},
    {"name": "Alex", "department": "HR"},
    {"name": "Mike", "department": "IT"},
]

grouped = {}

for user in users:

    department = user["department"]

    grouped.setdefault(department, []).append(user)

print(grouped)


# ============================================================
# 35. FIND DUPLICATES
# ============================================================

numbers = [1, 2, 3, 2, 4, 5, 1]

seen = set()
duplicates = []

for number in numbers:

    if number in seen:
        duplicates.append(number)
    else:
        seen.add(number)

print(duplicates)


# ============================================================
# 36. FREQUENCY COUNT
# ============================================================

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)


# ============================================================
# 37. CHUNK LIST
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chunk_size = 3

chunks = [
    numbers[i:i + chunk_size]
    for i in range(0, len(numbers), chunk_size)
]

print(chunks)


# ============================================================
# 38. PAGINATION
# Very common in APIs
# ============================================================

users = list(range(1, 101))

page = 2
page_size = 10

start = (page - 1) * page_size
end = start + page_size

result = users[start:end]

print(result)


# ============================================================
# 39. API RESPONSE PROCESSING
# ============================================================

response = {
    "status": True,
    "data": [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alex"},
        {"id": 3, "name": "Mike"}
    ]
}

users = response.get("data", [])

for user in users:
    print(user.get("id"), user.get("name"))


# ============================================================
# 40. API RESPONSE - FILTER ACTIVE USERS
# ============================================================

response = {
    "data": [
        {"id": 1, "name": "John", "active": True},
        {"id": 2, "name": "Alex", "active": False},
        {"id": 3, "name": "Mike", "active": True}
    ]
}

active_users = [
    user
    for user in response.get("data", [])
    if user.get("active")
]

print(active_users)


# ============================================================
# 41. API RESPONSE - EXTRACT IDS
# ============================================================

ids = [
    user.get("id")
    for user in response.get("data", [])
]

print(ids)


# ============================================================
# 42. API RESPONSE - FIND BY ID
# ============================================================

user_id = 2

user = next(
    (
        user
        for user in response.get("data", [])
        if user.get("id") == user_id
    ),
    None
)

print(user)


# ============================================================
# 43. API RESPONSE - CHECK IF ID EXISTS
# ============================================================

user_id = 2

exists = any(
    user.get("id") == user_id
    for user in response.get("data", [])
)

print(exists)


# ============================================================
# 44. ANY / ALL
# ============================================================

numbers = [2, 4, 6, 8]

print(any(x > 5 for x in numbers))
print(all(x % 2 == 0 for x in numbers))


# ============================================================
# 45. LIST + DICT CONVERSION
# ============================================================

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alex"},
    {"id": 3, "name": "Mike"},
]

user_dict = {
    user["id"]: user
    for user in users
}

print(user_dict)


# ============================================================
# 46. LIST OF IDS -> LIST OF OBJECTS
# ============================================================

user_ids = [1, 2, 3]

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alex"},
    {"id": 3, "name": "Mike"},
]

result = [
    user
    for user in users
    if user["id"] in user_ids
]

print(result)


# ============================================================
# 47. REMOVE NONE / EMPTY VALUES
# ============================================================

data = [
    10,
    None,
    "",
    20,
    [],
    30,
    False
]

result = [x for x in data if x]

print(result)


# ============================================================
# 48. COPY LIST
# ============================================================

numbers = [1, 2, 3]

copy1 = numbers.copy()
copy2 = numbers[:]
copy3 = list(numbers)


# ============================================================
# 49. SHALLOW COPY WITH NESTED LIST
# ============================================================

data = [[1, 2], [3, 4]]

copy_data = data.copy()

copy_data[0].append(100)

print(data)
print(copy_data)


# ============================================================
# 50. DEEP COPY
# ============================================================

import copy

data = [[1, 2], [3, 4]]

copy_data = copy.deepcopy(data)

copy_data[0].append(100)

print(data)
print(copy_data)

# PRACTICE QUESTIONS
#
# 1. Find all users whose age > 30
#
# 2. Find the user with the highest salary
#
# 3. Find the second-highest salary
#
# 4. Remove duplicate users based on user_id
#
# 5. Find duplicate user_ids
#
# 6. Count users department-wise
#
# 7. Return only user names
#
# 8. Return only active users
#
# 9. Find user by user_id
#
# 10. Check whether a particular user_id exists
#
# 11. Sort users by salary
#
# 12. Sort users by salary descending
#
# 13. Sort users by name
#
# 14. Group users by department
#
# 15. Find departments having more than 2 users
#
# 16. Flatten nested API response
#
# 17. Remove None values
#
# 18. Remove duplicate values while preserving order
#
# 19. Split 100 records into batches of 10
#
# 20. Implement pagination manually
#
# 21. Merge two lists
#
# 22. Find common elements between two lists
#
# 23. Find elements present in list A but not list B
#
# 24. Find missing IDs
#
# 25. Find frequency of each value
#
# 26. Convert list of dictionaries into dictionary by ID
#
# 27. Convert dictionary back into list
#
# 28. Find first matching record
#
# 29. Find all matching records
#
# 30. Handle API response when "data" is missing