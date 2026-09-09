# Class
# Object
# Constructor
# Self (instance variable)
# Encapsulation


# OOPS(Object-Oriented Programming System) is a programming paradigm that uses objects and classes to structure code. 
    # It allows for encapsulation, inheritance, and polymorphism, making it easier to manage and maintain complex software systems.

# Class:
    # A class is a blueprint for creating objects. It defines the properties (attributes) and
      # behaviors (methods) that the objects created from the class will have.
# Object:
    # An object is an instance of a class. It is created based on the class definition.
    # It helps to retrun the values using through the class and its methods.

# Syntax of class:

# class ClassName:
#     constructor (def __init__)
#     def FunctionName:
#         Block of code
#     def FunctionName:
#         Block of code
# obj = ClassName()  # Creating an object of the class
# obj.FunctionName()  # Calling a method of the class using the object


# Example A function without class:
def print_brand():
    print("Brand: BMW M4 CS")

print_brand()  # This function will access anywhere in the program, So it's not secure.

# Example A function with class:
class Car:
    def Brand(self):
        print("Brand: BMW M2")
obj = Car()  # Creating an object of the class
obj.Brand()  # Calling a method of the class using the object


# Constructor:
    # A constructor is a special method in a class that is automatically called when an object 
      # of the class is created. It is used to initialize the attributes of the object.

class Test:
    def __init__(self, a):
        self.a = a
        # Using the __init__() method, we can assign the a value to the whole class.
        # The word (Self) refers to the instance of the class, we can name it anything we want.
    def display(self):
        print("Value of a:",self.a)
    def display1(self):
        print("Value of b:",self.a)
obj = Test(5)  # Creating an object of the class
obj.display()  # Calling a method of the class using the object
obj.display1()  # Calling a method of the class using the object


class Student:
    def __init__(self, name, age, Fees, Marks):
        self.name = name  # Instance variable(Local Variable) for name
        self.age = age    # Instance variable(Local Variable) for age
        self.Fees = Fees  # Instance variable(Local Variable) for Fees
        self.Marks = Marks# Instance variable(Local Variable) for Marks

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Fees: {self.Fees}")
    def display_marks(self):
        print(f"{self.name}'s Your Marks: {self.Marks}")
Student1 = Student("Toji", 20, 50000, 85)  # Creating an object of the class
Student2 = Student("Nezuko", 18, 45000, 90)  # Creating an object of the class
Student1.display_info()  # Calling a method of the class using the object
Student2.display_marks()
Student2.display_info()  # Calling a method of the class using the object
Student1.display_marks()


# Encapsulation:
    # Encapsulation is the process of bundling data (variables) and methods (functions) 
     # that operate on the data into a single unit, 
      # i.e.,  class + Variable + Function = Encapsulation.
   