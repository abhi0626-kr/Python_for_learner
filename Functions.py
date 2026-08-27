# Functions :

#     Function is a block of code, which can be used multiple times. 
#     It allows us to write a code once and use it multiple times.
#     Functions help in reducing code redundancy and improve code reusability.
#     Functions are two types:
#         I. Built-in Functions.
#           1. print() -> It is used to print the output on the console.
#           2. input() -> It is used to take input from the user.
#           3. len() -> It is used to find the length of a string, list, tuple, etc.
#           4. type() -> It is used to find the data type of a variable.
#           5. range() -> It is used to generate a sequence of numbers.
#           6. sum() -> It is used to find the sum of all elements in a list, tuple, etc.
#           7. max() -> It is used to find the maximum element in a list, tuple, etc.
#           8. min() -> It is used to find the minimum element in a list, tuple, etc.
#           9. sorted() -> It is used to sort the elements in a list, tuple, etc.
#           10. abs() -> It is used to find the absolute value of a number.  
#           11. round() -> It is used to round a number to the nearest integer.
#           12. isinstance() -> It is used to check if an object is an instance of a class or a subclass thereof.
#           13. all() -> It is used to check if all elements in an iterable are true.
#           14. any() -> It is used to check if any element in an iterable is true.
#           15. enumerate() -> It is used to add a counter to an iterable and returns it in a form of enumerate object.
#           16. zip() -> It is used to combine two or more iterables (lists, tuples, etc.) into a single iterable.


#         II. User-defined Functions.
#           syntax:
#               def function_name(parameters):
#                   code block or Execution block
#                   return
#           calling a function:
#               function_name(arguments)

# Function -> Function definition -> Function Call
# Parameters & Arguments.
# *args and **kwargs.
# local and global variables.
# print() and return statement.
# Libraries -> Installation of Libraries -> Importing Libraries -> Using Libraries.


# User-defined Functions :


def greet(): # greet() is a function.
    N = input("Enter your name: ")
    print(f"Hello, {N}!")
greet()

def greeting(name, age): # (name, age) are parameters.
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello, {name}! You are {age} years old.")
greeting("name", "age")


def Greet(name):
    print(f"Hello, {name}! Welcome to the world of Python.")
Greet("Sukuna") # (Sukuna) is an argument.


# Write a function to find the sum n of  numbers.
def find_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(find_sum(5))


# Write a program for calculator using functions. 

def calcul(a,b,symbol):
    if symbol == "+":
        return a + b
    elif symbol == "-":
        return a - b
    elif symbol == "*":
        return a * b
    elif symbol == "/":
        return a / b
    else:
        return "Invalid symbol"

print(calcul(10, 10, "+"))


# *args -> class(Tuple) and **kwargs:------------------------------------------------------------------------

# In functions, parameters are allowed to have one agrument for one parameter. 
# But using the *args and **kwargs, we can pass multiple arguments to a function.


# Write a program for calculator using functions. 

def calculate(symbol, *args): # Using *args.
    if symbol == "+":
        return sum(args)
    elif symbol == "-":
        return args[0] - sum(args[1:])
    elif symbol == "*":
        return args[0] * args[1]
    elif symbol == "/":
        return args[0] / args[1]
    else:
        return "Invalid symbol"

print(calculate("/", 10, 0))


# **kwargs: It is used to pass a variable number of keyword arguments to a function.

def test(**kwargs): # Using **kwargs.
    print(kwargs)
test(name="Sukuna", age=20, city="Tokyo")


# Write a program to Add list of all numbers using *args and **kwargs.

def add_numbers(*args, **kwargs):
    total = sum(args)
    for key, value in kwargs.items():
        if type(value) == int or type(value) == float:
            total += value
    return total

# print(add_numbers(1, 2, 3, True, a=4, b=5, c=6)) # Now it can also add the values mentioned in the variable arguments. It will ignore the non-numeric values.


# Return Statement: It is used to return a value from a function.---------------------------

# Diiference between print() and return statement:
# print() -> It is used to print the output on the console. It does not allow to store the output in a variable.
# return -> It is used to return a value from a function. It does allow to store the output in a variable.
def add(a, b):
    n = a + b
    return n # It store the output in a variable : n.


# Local and Global Variables:-----------------------------------------------
# Local variables are defined inside a function and can only be accessed inside that function.
# Global variables are defined outside a function and can be accessed anywhere in the program.

A = "Global Variable"

def local_variable():
    B = "Local Variable"
    # return A # It will print the local variable.
    print(A, B)


local_variable() # It will print the local variable.
# # print(local_variable())
# print(A) # It will print the global variable.


# Convert a local variable to a global variable using the global keyword.
def convert_to_global():
    global C # It will convert the local variable to a global variable.
    C = "Global Variable"
    print(C)

convert_to_global() # It will print the global variable.
print(C) # It will print the global variable.


# Update a global variable using the global keyword.
# It's overriding the global variable with a new value.
High_Score = 100

def update_score():
    global High_Score # It will update the global variable.
    High_Score = 200
    print(High_Score)

update_score() # It will print the updated global variable.
print(High_Score) # It will print the updated global variable.



# f-string : print(f"")

a = 50
b = 11

print("The sum of", a, "and", b, "is", a + b) # It will print the sum of a and b.
# Using the (f-string).
print(f"The sum of {a} and {b} is {a + b}.") # It also print the sum of a and b.



