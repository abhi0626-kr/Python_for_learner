#For loop
#For loop used to run the statement or group of statement or block of code.
#For loop is highly work on Advance Datatype (List, tuple, Dictionary, Set) and only work with string in standard Datatype.

#syntax of For loop.
# for Temp_variable/Loop_variable in variable /range_Function :
#     block of code/execution statement

#The X contain only the standard datatype (String)
x = "Hello_world"
for i in x:
    print(i)

#It return the print value for N number of times, N contains "python" as [p-1, y-2, t-3, h-4, o-5, n-6] , So N =6 
N = 'python'
for i in N:
    print('Abhishek')

#Now the X contains the list value of (str,int,float,bool), it return all 
x = ["Abhishek", 23, 11.11, True]
for i in x:
    print(i)

#write a program to print only the constant character
n = 'This is a python class '
for i in n:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        print(i)


#Range function
#Range function is used to generate the sequence of number, it return the integer value only.
#Here the range function is used to generate the sequence of number from 1 to 10 with the step value of 2.
for i in range(0,100,2): #0 = start, 100 = stop, 2 = step
    print(i)

n = int(input("Enter the number: "))
for i in range(0,n,2): #0 = start, n = stop, 2 = step
    print(i)    


x = 101
for i in range(0,x+1): #0 = start, 101 + 1 = stop
    print(i)




#nested for loop
#Nested for loop is used to run the for loop inside the for loop, it is used to run the for loop multiple times, it is used to run the for loop inside the for loop.
#Combination

color = ['Red', 'Green', 'Blue'] #Outer Loop
things = ['Car', 'Bike', 'Bus'] #Inner Loop
for i in color:
    for j in things:
        print(i, j)

B =["Alex", "David", "lara", "Sam"]
C = ["Black", "Red", "Blue"]
D = ["Box","Clothes", "Car"]
for i in C:
    for j in D:
        if 'l' in C:
            continue
        for k in B:
                print(i, j, k)




#Write a program to generate the multiplication table from 2 to given n number
n = input("Enter the number: ")
if n.isdigit():
    n = int(n)

    if n>= 2:
        for i in range(2, n+1):
            for j in range(1, 13):
                print(i, "x", j, "=", i*j)
            print("\n")
    else:
       print("Please enter a number greater than 2.")
else:
    print("Please enter a valid number.")




