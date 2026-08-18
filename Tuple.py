#Advance Data types.

#Tuple .
# Tuple is one of the 4 built-in data types.
# Tuple is ordered, unchangeable, and allows duplicate values.
# Tuple is written with ()parentheses.
# Tuple can contain any data type, including other tuples.
# Tuple is Indexed and immutable, eg.(int,str,float,bool,complex,tuple,set,dictionary and Tuple too)
# We can use the tuple() function to make a tuple.
# Tuple can not be change, edit, or delete items after it has been created.

# Both are empty tuples, but they are created using different methods. The first one is created using parentheses, while the second one is created using the tuple() function.

tpl = () #Empty Tuple
x = tuple() #Empty Tuple using tuple() function


# Using the comma after the string to create a single-element tuple, otherwise it will be considered as a string.
tpl = ('hello',) 
print(type(tpl)) #('hello',)
# OR
tpl = ('hello')
print(type(tpl)) #<class 'str'>

# Operations on Tuple:
# 1. Indexing
# 2. Comprehension
# 3. we cannot insert, update, delete or pop items in a tuple after it has been created.

