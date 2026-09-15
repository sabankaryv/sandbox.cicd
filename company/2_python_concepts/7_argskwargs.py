# What is args?
# args* is used when we want a function to accept a variable number of positional arguments.
# Inside the function, all those arguments are collected into a tuple
# The name args is just a convention; the important part is the *.

# Example
# We use *args when we want a function to accept any number of values.
def add(*args):
    return sum(args)

print(add(10, 20, 30))

# what is kwargs?
# **kwargs allows a function to accept multiple keyword arguments. These arguments are stored as a dictionary.
def student(**kwargs):
    print(kwargs)

student(name="Yogesh", age=35, city="Pune")
# *args is for multiple positional arguments, while **kwargs is for multiple keyword arguments.