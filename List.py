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


# Wirte a program to add 1 - 100 in the List.
x = []
for i in range (1, 101):
    x.append(i)
    print(x)


# # Wirte a program to add 1 - 100 in the enev numbers in even list and odd numbers in odd list.
even_lst=[]
odd_lst=[]

for i in range(1,101):
    if i %2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("Even List:", even_lst)
print("Odd List:", odd_lst)

# Write a program to add 1 - 100 in the enev numbers in even list and odd numbers in odd list using List Comprehension.
even_lst = [i for i in range(1, 101) if i % 2 == 0]
odd_lst = [i for i in range(1, 101) if i % 2 != 0]

print("Even List:", even_lst)
print("Odd List:", odd_lst)

# POP cannot be used in Loops
x = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
 
for i in range(len(x)):
    if x[i] ==5:
        x.pop()

        
# # Write a program to find the largest number in the list without using max() function.

x = [0,1,1,2,3,5,8,13,21,34]
largest = x[0]

for i in range(1, len(x)):
    if x[i] > largest:
        largest = x[i]

print("The largest number in the list is:", largest)



# Write a program to find the second largest number in the list without using max() function.

x = [0,1,1,2,3,5,8,13,21,34]
second_largest = x[0]
largest = x[0]
for i in x:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("The second largest number in the list is:", second_largest)



# Given an List of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

a = [2,7,11,15]

target = 26

for i in range(len(a)):
    for j in range(1, len(a) -1):
        if i != j:
            if a[i] + a[j] == target:
                print([i,j], [a[i], a[j]], "=", target)
                break


# List Comprehension.
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if 'a' in x:
        new_list.append(x)
        
print(new_list)

print("List Comprehension")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if 'a' in x]
print(new_list)



# List Sorting.

# There are two types of sorting in List:
# 1. Ascending Order: from smallest to largest.
# 2. Descending Order: from largest to smallest.

# Sort() method is used to sort the list in ascending order by default.

list = [100, 50, 65, 82, 23]
list.sort()
print(list) # Output: [23, 50, 65, 82,100]

#Sort() using reverse=True parameter sorts the list in descending order.
list.sort(reverse=True)
print(list) # Output: [100, 82, 65, 50, 23]

# The reverse()
# The reverse() method reverses the current order of the list.
list.reverse()
print(list) # Output: [23, 50, 65, 82, 100]

#reverse with reversed() function using index value.
x = list[::-1]
print(x)


# In the string list, the sort() method sorts the list Uppercase letters first, followed by lowercase letters. 
List = ["af", "Oe", "Kia", "che", "Bmw", "Audi"]
List.sort()
print(List) # Output: ['Audi', 'Bmw', 'Kia', 'Oe', 'af', 'che']


# # Check the given values is palindrome or not.
x = "madam"

y = x[::-1]
if x == y:
    print(x," = The given value is palindrome")
else:
    print(x,"The given value is not palindrome")
