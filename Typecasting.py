# #Typecasting 

# #float - int.
# n = 684.98
# print(type(n))
# n1 = (int(n))
# print(type(n1))
# print("---------------------------")
# #str - float 
# n = "6111.11"
# print(type(n))
# n1 = (float(n))
# print(type(n1))
# print("---------------------------")

# #str - int
# n = "5678"
# print(type(n))
# n1 = (int(n))
# print(type(n1))
# print("---------------------------")

# #str - boole
# n = "123"
# print(type(n))
# n1 = (bool(n))
# print(type(n1))
# print("---------------------------")

# #int - bool
# n = 0
# print(type(n))
# n1 = (bool(n))
# print(type(n1))
# print("---------------------------")

# #float - bool
# n = 200.5
# print(type(n))
# n1 = (bool(n))
# print(type(n1))
# print("---------------------------")


# #List
# #list - tuple
# L = [1,2,3,4,5,6]
# print(type(L))
# L1 = (tuple(L))
# print(L1)
# print(type(L1))
# print("---------------------------")

# #list - dictionary
# import numpy as np 

# L = [1,2,3,4,5,6]
# print(type(L))
# L1 = np.array(L)
# print(L1)
# print(type(L1))
# print("---------------------------")

# #list - set
# L = [1,2,3,4,5,6]
# print(type(L))
# L1 = (set(L))
# print(L1)
# print(type(L1))
# print("---------------------------")



# #Dictionary

# #Dictionary - list
# #when we use to convert the "dict" value to "list" it only return the '(Label)' name of the dictionary value. 

# D = {"name":'Abhi', "hobbiies": 'Calisthenics, Running' }
# print(D)
# D1 = (list(D))
# print(D1)
# print(type(D1))
# print("---------------------------")

# #Dictionary - set
# #when we use to convert the "dict" value to "set" it also only return the '(Label)' name of the dictionary value. 


# D = {"name":'Abhi', "hobbiies": 'Calisthenics, Running' }
# print(D)
# D1 = (set(D))
# print(D1)
# print(type(D1))
# print("---------------------------")

# #Dictionary - Tuple
# #when we use to convert the "dict" value to "list" it also only return the '(Label)' name of the dictionary value. 


# D = {"name":'Abhi', "hobbiies": 'Calisthenics, Running' }
# print(D)
# D1 = (tuple(D))
# print(D1)
# print(type(D1))
# print("---------------------------")

# #Dictionary - Array
# import numpy as np
# D = {"name":'Abhi', "hobbiies": 'Calisthenics, Running' }
# print(D)
# D1 = (np.array(D))
# print(D1)
# print(type(D1))
# print("---------------------------")


# #Tuple 

# #Tuple - list
# T = ["Abhishek", 20, 9.9, ]
# print(T)
# T1 = (list(T))
# print(type(T1))
# print("------------------------------")

# #Tuple - set 
# T = ["Abhishek", 20, 9.9, ]
# print(T)
# T1 = (set(T))
# print(type(T1))
# print("------------------------------")

# #Tuple - Dictionary
# #Tuple - Dictionary is not possible to convert because we a (lable or key values) for that.

# #Tuple - Array
# import numpy as np 

# T = ["Abhishek", 20, 9.9, ]
# print(T)
# T1 = (np.array(T))
# print(type(T1))
# print("------------------------------")

# #Set()
# #Set - List
# S = {"Ahbishek","Calisthanics", "Gym", "Running" }
# print(S)
# S1 = (list(S))
# print(type(S1))

# #Set - Tuple
# S = {"Ahbishek","Calisthanics", "Gym", "Running" }
# print(S)
# S1 = (tuple(S))
# print(type(S1))

# #set - Dictionary
# #Set - Dictionary is not possible to convert because we a (lable or key values) for that.

# #set - Array
# import numpy as np
# S = {"Ahbishek","Calisthanics", "Gym", "Running" }
# print(S)
# S1 = (np.array(S))
# print(type(S1))

