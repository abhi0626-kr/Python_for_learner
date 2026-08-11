#Advance Data types.

#List .
# List is one of the 4 built-in data types.
# List is ordered, changeable, and allows duplicate values.
# List is written with []square brackets.
# List can contain any data type, including other lists.
# List is Indexed and mutable, eg.(int,str,float,bool,complex,tuple,set,dictionary and List too)
# We can use the list() function to make a list.


# Both are empty lists, but they are created using different methods. The first one is created using square brackets, while the second one is created using the list() function.
from sympy import li


List = [] #Empty List
x = list() #Empty List using list() function


# What is Indexing in List?
# Indexing is a way to access individual elements in a list using their position or index.

# Two types of indexing in List:
# 1. Positive Indexing: starts from 0 to +infinity.
# 2. Negative Indexing: starts from -1 to -infinity.

list1 = [1, 2, 3, "Python", 5, "Learn"]
print(list1[4]) # Output: 5
print(list1[-1]) # Output: "Learn"
print(list1[-0]) # Output: 1
print(type(list1)) # Output: <class 'list'>
print(type(list1[3])) # Output: <class 'str'>

#Range of Indexing in List
print(list1[4:1]) # Output: [2, 3, "Python"]
print(list1[-4:-1]) # Output: [2, 3, "Python"]
print(list1[1:]) # Output: [2, 3, "Python", 5, "Learn"]
print(list1[:4]) # Output: [1, 2, 3, "Python"]
print(list1[1:4:2]) # Output: [2, "Python"]




# List Operations:

# Insert
# append
# Extend
# Remove
# pop
# update