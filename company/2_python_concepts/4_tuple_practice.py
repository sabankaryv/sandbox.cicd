# ============================================================
# 4_tuple_practice.py
# TUPLE PRACTICE - Python + API + Battle Preparation
# ============================================================


# ============================================================
# 1. CREATE TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers)


# Single element tuple

value = (10,)

print(value)
print(type(value))


# Without brackets

numbers = 10, 20, 30

print(numbers)


# ============================================================
# 2. ACCESS ELEMENTS
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[-1])


# ============================================================
# 3. SLICING
# ============================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# ============================================================
# 4. LOOP
# ============================================================

numbers = (10, 20, 30)

for number in numbers:
    print(number)


# ============================================================
# 5. LENGTH
# ============================================================

numbers = (10, 20, 30)

print(len(numbers))


# ============================================================
# 6. COUNT
# ============================================================

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))


# ============================================================
# 7. INDEX
# ============================================================

numbers = (10, 20, 30)

print(numbers.index(20))


# ============================================================
# 8. CHECK EXISTENCE
# ============================================================

numbers = (10, 20, 30)

print(20 in numbers)
print(100 in numbers)


# ============================================================
# 9. CONCATENATION
# ============================================================

a = (1, 2, 3)
b = (4, 5, 6)

result = a + b

print(result)


# ============================================================
# 10. REPETITION
# ============================================================

numbers = (1, 2)

print(numbers * 3)


# ============================================================
# 11. UNPACKING
# ============================================================

data = (101, "John", 30)

user_id, name, age = data

print(user_id)
print(name)
print(age)


# ============================================================
# 12. STAR UNPACKING
# ============================================================

data = (1, 2, 3, 4, 5)

first, *middle, last = data

print(first)
print(middle)
print(last)


# ============================================================
# 13. SWAP VALUES
# ============================================================

a = 10
b = 20

a, b = b, a

print(a)
print(b)


# ============================================================
# 14. TUPLE FROM LIST
# ============================================================

numbers = [1, 2, 3, 4]

result = tuple(numbers)

print(result)


# ============================================================
# 15. LIST FROM TUPLE
# ============================================================

numbers = (1, 2, 3, 4)

result = list(numbers)

print(result)


# ============================================================
# 16. NESTED TUPLE
# ============================================================

data = (
    (1, "John"),
    (2, "Alex"),
    (3, "Mike")
)

print(data[0])
print(data[0][1])


# ============================================================
# 17. TUPLE OF DICTIONARIES
# ============================================================

users = (
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Alex"}
)

for user in users:
    print(user["name"])


# ============================================================
# 18. TUPLE AS DICTIONARY KEY
# Very important
# ============================================================

data = {
    (101, "/orders"): 2,
    (102, "/users"): 2
}

print(data)


# ============================================================
# 19. API STYLE RESPONSE
# ============================================================

response = (
    200,
    "success",
    [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alex"}
    ]
)

status, message, users = response

print(status)
print(message)
print(users)


# ============================================================
# 20. FUNCTION RETURNING MULTIPLE VALUES
# ============================================================

def get_user():

    return 101, "John", 50000


user_id, name, salary = get_user()

print(user_id)
print(name)
print(salary)


# ============================================================
# 21. ZIP RETURNS TUPLES
# ============================================================

names = ["John", "Alex", "Mike"]
ages = [25, 30, 28]

result = list(zip(names, ages))

print(result)


# ============================================================
# 22. SORT TUPLES
# ============================================================

data = [
    ("John", 50000),
    ("Alex", 70000),
    ("Mike", 60000)
]

result = sorted(data, key=lambda x: x[1])

print(result)


# ============================================================
# 23. FIND MAX/MIN
# ============================================================

data = [
    ("John", 50000),
    ("Alex", 70000),
    ("Mike", 60000)
]

print(max(data, key=lambda x: x[1]))
print(min(data, key=lambda x: x[1]))


# ============================================================
# 24. IMMUTABILITY
# ============================================================

data = (10, 20, 30)

# data[0] = 100
# TypeError


# ============================================================
# 25. TUPLE CONTAINING MUTABLE OBJECT
# Important concept
# ============================================================

data = ([1, 2], [3, 4])

data[0].append(100)

print(data)


# ============================================================
# 26. REMOVE DUPLICATES
# ============================================================

data = (1, 2, 2, 3, 3, 4)

result = tuple(set(data))

print(result)


# ============================================================
# 27. CONVERT LIST OF LIST INTO TUPLES
# ============================================================

data = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = [tuple(item) for item in data]

print(result)


# 1. Why is tuple immutable?
#
# 2. Why can tuple be used as dictionary key?
#
# 3. Can tuple contain a list?
#
# 4. Is tuple always immutable internally?
#
# 5. Difference between tuple and list?
#
# 6. Why is (10) not a tuple?
#
# 7. How do you create a single-element tuple?
#
# 8. How does tuple unpacking work?
#
# 9. What is * unpacking?
#
# 10. Why does zip() produce tuples?
#
# 11. How can a function return multiple values?
#
# 12. How do you sort tuple data?