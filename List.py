#Advance Data types.

#List .
# List is one of the 4 built-in data types.
# List is ordered, changeable, and allows duplicate values.
# List is written with []square brackets.
# List can contain any data type, including other lists.
# List is Indexed and mutable, eg.(int,str,float,bool,complex,tuple,set,dictionary and List too)
# We can use the list() function to make a list.


# Both are empty lists, but they are created using different methods. The first one is created using square brackets, while the second one is created using the list() function.



List = [] #Empty List
x = list() #Empty List using list() function


# What is Indexing in List?
# Indexing is a way to access individual elements in a list using their position or index.

# Two types of indexing in List:
# 1. Positive Indexing: starts from 0 to +infinity.
# 2. Negative Indexing: starts from -1 to -infinity.

list1 = [1, 2, 3, "Python", 5, "Learn", True, 3.14, 9, 10, 11.11, 'AI', 13]
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
print(list1[-4:-1:-2]) # Output: []
print(list1[-1:-8:-1]) # Output: [13, 'AI', 11.11, 10, 9, 3.14, True]

# List Operations:

# Insert
# Using Insert a new value in any position(index) in the list 
n = [1, 2, 3, "Python", 5, "Learn", True, 3.14, 9, 10, 11.11, 'AI', 13, 14]

n.insert(1, "New Value") # Insert a new value at index 1
# Output: [1, 'New Value', 2, 3, 'Python', 5, 'Learn', True, 3.14, 9, 10, 11.11, 'AI', 13, 14]

n.insert(-1,13.50)
# Output: [1, 2, 3, 'Python', 5, 'Learn', True, 3.14, 9, 10, 11.11, 'AI', 13, 13.5, 14]

n.insert(2,("New", "Tuple"))
print(n[2]) # Output: ('New', 'Tuple')
# Output; [1, 2, ('New', 'Tuple'), 3, 'Python', 5, 'Learn', True, 3.14, 9, 10, 11.11, 'AI', 13, 14]
print(n) 


# append
# Append() can only take one value at a time.
# Append() always add the new value in the end of the list
n.append(15)
print(n) 
# Output: [1, 2, 3, 'Python', 5, 'Learn', True, 3.14, 9, 10, 11.11, 'AI', 13, 14, 15]



# # Extend
# # Extend() is use to add a new (set or group) of value in the end of the List.
a = [1, 2, 3, "Python", 5, "Learn"]
b = (12, 22, 22.2, 445)
a.extend(b) 
print(a)
# Output :[1, 2, 3, 'Python', 5, 'Learn', 12, 22, 22.2, 445]


# update
# Update a value in the list using index.
a[2] = "New Value" 
# Output: [1, 2, 'New Value', 'Python', 5, 'Learn', 12, 22, 22.2, 445]

# pop
# pop() is used to remove a value from the list using index.
a.pop()
print(a) # Output: [1, 2, 3, "Python", 5,]





