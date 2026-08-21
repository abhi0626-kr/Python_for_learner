# Set dose not allow duplicate values. 
# It is an unordered collection of data type that is iterable.
# mutable and has no duplicate elements.
# We can not change values, but we can delete & add a new value .
# set is not indexed, it dose not have a key.
# set is written with {} curly brackets.

# True and 1 are considered the same value in set, and only one of them will be stored.
# False and 0 are also considered the same value in set, and only one of them will be stored.
# st = set() #Empty Set

# st = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #Set with integer values
# print(st) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# st = {1,1,1,2,2,3,4,5,6,6,3}
# print(st) # Output: {1, 2, 3, 4, 5, 6} # It will remove the duplicate values.

thisset = {"Python", 1, 2.5, True, (1, 2, 3), "Python", 1}
print(thisset) # Output: {True, 1, 2.5, (1, 2, 3), 'Python'} # It will remove the duplicate values.

# To add a new value to the set, we can use the add() method.
thisset.add("C++") # Output: None # It will add the new value to the set.
print(thisset)

# To delete a value from the set, we can use the discard() method.
# Discard() will allow to delete the value is mot in the set.
thisset.discard("Python") # Output: None # It will delete the specified value from the set.
print(thisset)


# Join two sets using the :

# union() method.
# intersection() method 
# difference() method
# symmetric_difference() method
# union_update() method
# intersection_update() method
# difference_update() method
# symmetric_difference_update() method


# Union of two sets using the union() method.
set1 = {"a", "b", "c", "d", "e"}
set2 = {4, 5, 6, 7, 8}
set3 = {'Toji', 'Megumi', 'Yuji', 'Sukuna'}
new_set = set1.union(set2, set3)
new_set1 = set1 | set2 | set3
print(new_set) # Output: {'a', 'b', 'c', 'd', 'e', 4, 5, 6, 7, 8, 'Toji', 'Megumi', 'Yuji', 'Sukuna'} # It will return a new set with all the unique values from all sets.
print(new_set1) # Output: {'a', 'b', 'c', 'd', 'e', 4, 5, 6, 7, 8, 'Toji', 'Megumi', 'Yuji', 'Sukuna'} # It will return a new set with all the unique values from all sets.

# set1.update(set2, set3)
print(set1) # Output: {'a', 'b', 'c', 'd', 'e', 4, 5, 6, 7, 8, 'Toji', 'Megumi', 'Yuji', 'Sukuna'} # It will return a new set with all the unique values from all sets.

# Intersection : 
        # Join 2 or more set, only take the common values from all sets.

set1 = {"a", "b", "c", "d", "e"}
set2 = {"Toji", "Megumi", "Yuji", "Sukuna","a"}
new_set = set1.intersection(set2)
print("new_set:", new_set) # Output: set() # It will return a new set with all the common values from all sets.

set1.intersection_update(set2)
print("set1:", set1) # Output: set() # It will return a new set with all the


set1 = {"a", "b", "c", "d", "e"}
set2 = {"Toji", "Megumi", "Yuji", "Sukuna","a"}
set3 = {"Toji", "obito"}
set4 = {"obito", "1", "2", "3", "4", "5"}

intersection_set = set1.intersection(set2, set3, set4)
intersection_set1 = set1 & set2 & set3 & set4
print("intersection_set:", intersection_set) # Output: set() # It will return a new


# Difference :
#         # Join 2 or more set, only take the unique values from the first set

set1 = {"a", "b", "c", "d", "e"}
set2 = {"Toji", "Megumi", "Yuji", "Sukuna","a"}
set3 = {"Toji", "obito", "b"}
set4 = {"obito", "1", "2", "3", "4", "5"}

Difference_set = set1.difference(set2)
print("Difference_set:", Difference_set) 
# Output: {'b', 'c', 'd', 'e'} # It will return a new set with the unique values from the first set.

Difference_set1 = set1.difference(set2, set3, set4)
print("Difference_set1:", Difference_set1) 
# Output: {'c', 'd', 'e'} # It will return a new set with the unique values from the first set.

set1.difference_update(set2)
print("set1:", set1)



# Symmetric Difference :
#         # Join 2 or more set, only take the unique values from all sets.

set1 = {"a", "b", "c", "d", "e"}
set2 = {"Toji", "Megumi", "Yuji", "Sukuna","a"}
set3 = {"Toji", "obito", "b"}
set4 = {"obito", "1", "2", "3", "4", "5"}

sym_diff = set1.symmetric_difference(set2);
# we can not give more than 1 set in symmetric_difference() method.
print("sym_diff:", sym_diff)
# But we can use the symmetric_difference() method multiple times to get the unique values from all sets.
_1sym_diff = set1.symmetric_difference(set2);
_2sym_diff = _1sym_diff.symmetric_difference(set3);
_3sym_diff = _2sym_diff.symmetric_difference(set4);
print("sym_diff:", _3sym_diff)


# Write a program to remove the duplicate values from the list without using inbuild fuctions set.
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11,33, 44, 55]

unique_lst = []
print("Method 1: ")
for i in lst:
    if i not in unique_lst:
        unique_lst.append(i)

print("Original list:", lst)
print("List without duplicates:", unique_lst)

print("\nMethod 2: ")
for idx, value in enumerate(unique_lst):
        if value in lst:
                lst.pop(idx)
print("Original list:", lst) 
# The pop() method helps to remove the duplicate values by 90%. not fully remove the duplicate values from the list.
        
         
    