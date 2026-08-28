# Exception Handling.

# Exceptions are errors that occur during the execution of a program.
# Common Built-in Exceptions Error in Python include 
#   `ValueError`, 
#   `TypeError`, 
#   `IndexError`, 
#   `KeyError`,
#   `ZeroDivisionError`,
#   `NameError`,
#   `AttributeError`,
#   `ImportError` / `ModuleNotFoundError`,
#   `FileNotFoundError`,
#   `IndentationError` / `SyntaxError`
#   `UnboundLocalError`,
#   `OverflowError`,
#   `StopIteration`,
#   `RuntimeError`,
#   `NotImplementedError`,
#   `PermissionError`


#  `try`, `except`, `else`, and `finally` blocks.

# Syntax:

# try:
#     block of code /piece of code
# except ExceptionName/Exception:
#     block of code to handle the exception

# else:
#     block of code / exceution statement if no exception occurs

# finally:
#     block of code / exceution statement that will always execute regardless of whether an exception occurs or not.


# Without using the try-except block.
n = int(input("Enter a number: "))
for i in range(n):
    print(i)
# User = Enter a number: Abc
# Output: ValueError: invalid literal for int() with base 10: 'Abc' in the console.


# ValueError.----------
# Exception Handling with try-except and elseblock. 
try:
    N = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid Number.")
else:
    for i in range(N):
        print(i)


# ZeroDivisionError.----------
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter another number: "))
    c = a / b
except ValueError:
    print("Invalid input! Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# The (Exception) is used to catch any other unexpected exceptions that may occur during the execution of the code.
except Exception: 
    print(f"An unexpected error occurred.")
else:
    print(f"The result of {a} divided by {b} is: {c}")
# Finally block is executed regardless of whether an exception occurred or not.
finally:
    print("Execution completed!, whether an error occurs or not.")

# raise ValueError.----------------

def vote(age):
    if age < 18:
# (raise ValueError) is used to rasise a error by the Developer.
        raise ValueError("You must be at least 18 years old to vote.")
    else:
        print("You are eligible to vote.")

vote(18)
vote(15)  # This will raise a ValueError and terminate the program.

#  Custom Error. ---------------------------------------------
# Create a Own or Custom Error message by the Developer.
class AgeError(Exception):
    def __init__(self, message):
        self.message = message
def voteing(age):
    if age < 18:
# (AgeError) is used to rasising a own error by the Developer.
        raise AgeError("You must be at least 18 years old to vote.")
    else:
        print("You are eligible to vote.")

voteing(18)
voteing(15) # AgeError: You must be at least 18 years old to vote.