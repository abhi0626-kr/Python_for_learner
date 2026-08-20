#Advance Data types.

#Dictionary .
# Dictionary is one of the 4 built-in data types.
# Dictionary is ordered, changeable, and does not allow duplicate keys.
# Dictionary is written with {key : value} curly brackets with key-value pairs.
# Dictionary can contain any data type, including other dictionaries.
# Dictionary is Indexed and mutable, eg.(int,str,float,bool,complex,tuple,set,dictionary and Dictionary too)
# We can use the dict() function to make a dictionary.
# Both adding & updating values in a dictionary is done using the same syntax.

# (
# In key we can give data type like (int,str,float,bool,complex,tuple,set,dictionary and List too)
# but in value we can give any data type like (int,str,float,bool,complex,tuple,set,dictionary and List too).
# )

# List is not accpetable as a key.
# Both are empty dictionaries, but they are created using different methods. The first one is created using curly brackets, while the second one is created using the dict() function.


dic = {} #Empty Dictionary
x = dict() #Empty Dictionary using dict() function

# Key - int, str, float, bool, tuple, set, dictionary.
# Value - int, str, float, bool, tuple, set, dictionary and List too.

dic = {"name": "Sukuna",
       "age": 20,
       "course": "Python",
       "language": ["Python", "C", "C++", "Java"],
       "skills": {"Python": "Intermediate", "C": "Beginner", "C++": "Beginner", "Java": "Beginner"}
       }

# Output: {'name': 'Sukuna', 'age': 20, 'course': 'Python', 'language': ['Python', 'C', 'C++', 'Java'], 'skills': {'Python': 'Intermediate', 'C': 'Beginner', 'C++': 'Beginner', 'Java': 'Beginner'}}
print(dic)
# Output: <class 'dict'>
print(type(dic["language"])) # Output: <class 'list'>

# To print the keys.
print(dic.keys()) 
# Output: dict_keys(['name', 'age', 'course', 'language', 'skills'])

thisdic = {
       "brand" : "BMW",
       "model" : "M4 CS",
       "year" : 2026,
       "color" : "Black",
       "price" : 1000000,
       "features" : ["Sunroof", "Leather Seats", "Navigation System", "Bluetooth"],
       "specifications" : {"Engine": "3.0L Twin-Turbo Inline-6", "Horsepower": 503, "Torque": 479, "0-60 mph": "3.8 seconds" },
       "year": 2027 
       }
print(thisdic)


stud_info = {}
stud_info["Name"] = "Toji"
stud_info["Age"] = 20
stud_info["Course"] = "Python"
stud_info["join_date"] = "" # Giving a empty string value to the key.

stud_info["Fees"] = 50000

#Updateing the int value
stud_info["Fees"] += 500
stud_info.update({"Department" : "Developer"}) 
# Adding a new key-value pair using the update() method.
# Using the update() we update or add new value.

stud_info["Course"] = "AI" # Duplicate key, will overwrite the previous value.
# The output : should contain the lastest value.
# Both adding & updating values in a dictionary is done using the same syntax.


# Delete.
del stud_info["Fees"]
stud_info.pop("Age") # Using pop() method to remove a key-value pair.
stud_info.popitem() # Using popitem() method to remove the last inserted key-value pair.
stud_info.clear() # Using clear() method to remove all key-value pairs from the dictionary.

print(stud_info)




thisdic = {
       "brand" : "BMW",
       "model" : "M4 CS",
       "year" : 2026,
       "color" : "Black",
       "price" : 1000000,
       "features" : ["Sunroof", "Leather Seats", "Navigation System", "Bluetooth"],
       "specifications" : {"Engine": "3.0L Twin-Turbo Inline-6", "Horsepower": 503, "Torque": 479, "0-60 mph": "3.8 seconds" },
       "year": 2027 
       }

print("Key + Value:")
for key, value in thisdic.items():
    print(f"{key}: {value}")

print("\nKeys:")
for i in thisdic.keys():
    print(i) # Output: Only return the keys of the dictionary.
    
print("\nValues:")
for j in thisdic.values():
    print(j) # Output: It only return the values of the dictionary.
    
print("\nKey + Value using zip():")
for x in zip(thisdic.keys(), thisdic.values()):
    print(x)
# Output: zip helps to zip the two for loop and It return both key & Value of the different for loop(i & j)


# write a program to check the string, each vowel in the string and count the number of vowels in the string using dictionary.

from numba import char


sentence = "This is a sample sentence to count the number of vowels in it."
print("method 1: ")
vowels = "aeiouAEIOU"
vowel_count = {}

for i in sentence:
    if i in vowels:
        vowel_count[i] = vowel_count.get(i, 0) + 1

print("Vowel Count:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")

print("\nmethod 2: ")
vowels = "aeiou"
vowel_dict = {}
for i in sentence:
    i = i.lower()
    if i in vowels:
        vowel_dict[i] +=1
    else:
       vowel_dict[i] = 1





EMP_Details = {}
count = int(input("Enter the number of employees: "))

while count > 0:
    emp_id = (input("Enter Employee ID: "))
    if emp_id in EMP_Details:
        print("Employee ID already exists. Please enter a unique ID.")
    else:
        emp_name = input("Enter Employee Name: ")
        emp_age = int(input("Enter Employee Age: "))
        emp_department = input("Enter Employee Department: ")
        emp_salary = float(input("Enter Employee Salary: "))

    EMP_Details[emp_id] = {
        "Name": emp_name,
        "Age": emp_age,
        "Department": emp_department,
        "Salary": emp_salary
    }
    count -= 1 # Decrement the count after each employee entry
    
print("\nEmployee Details:")
for key, value in EMP_Details.items():
    print(f"{key}: {value}")