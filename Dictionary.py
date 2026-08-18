#Advance Data types.

#Dictionary .
# Dictionary is one of the 4 built-in data types.
# Dictionary is ordered, changeable, and does not allow duplicate keys.
# Dictionary is written with {key : value} curly brackets with key-value pairs.
# Dictionary can contain any data type, including other dictionaries.
# Dictionary is Indexed and mutable, eg.(int,str,float,bool,complex,tuple,set,dictionary and Dictionary too)
# We can use the dict() function to make a dictionary.

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