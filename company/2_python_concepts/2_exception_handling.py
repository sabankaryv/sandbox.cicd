"""
1.What is Exception Handling.
==> The Process of converting the technical error messages into the user friendly error messages is called exception handling.
"""

try:
    x=10/0
except ZeroDivisionError as e:
    print("Number Can not be devided by zero..",e)
finally:
    print("This Will Be executed always")

"""
2.What is the purpose of the finally block?
==> finally block contain the code that executed no matter exception occured or not.
==> 
"""

try:
    x=10/0
except ZeroDivisionError as e:
    print("Number Can Not be Devided by 0")
finally:
    print("This Block Will Always Be Executed...")

try:
    number=int(input("Enter The Number: "))
except ZeroDivisionError,ValueError:
    