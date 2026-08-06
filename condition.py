# Conditions Statement

#If, Elif, else statements

print("Conditions Statement")
A = int(input("Enter a number: "))
B = int(input("Enter another number: "))
C = int(input("Enter a third number: "))
D = int(input("Enter a fourth number: "))

if A < B and A < C and A < D:
    print("First value is less than all other values")
    
elif B < C and B < D and B < A:
    print("Second value is less than all other values")
    
elif C < A and C < B and C < D:
    print("Third value is less than all other values")
    
elif D < A and D < B and D < C:
    print("Fourth value is less than all other values")
    
else:
    print("No single value is less than all others")

print("----------------------------------------------------------------------------------------------------")



#nested if statement
#If inside a if is called nested if statement.
print("Nested If Statement option 1")

N = int(input("Enter a number: "))
if N>=80:
    print("Grade A")
    if N>=95 and N<=100:
        print("Excellent")
    else:
        print("Good")
else:
    print("Grade B")
    if N>=70 and N<80:
        print("Average")
    else:
        print("Poor")       


print("---------------------------------------------------------------------------------------")

print("Nested If Statement option 2 with elif")

#Based on the mark find the grade of the student using elif statement.

N = int(input("Enter a number: "))
if N>=80:
    print("Grade A")
elif N>=95 and N<=100:
    print("Excellent")
elif N>=70 and N<80:
    print("Average")
elif N<70:
    print("Grade B")
elif N<=60:  
    print("Grade C")    
elif N<50 and N>=40:
    print("poor")    
else:
    print("fail")              


#write a program for a simple calculator if statement


print("---------------------------------------------------------------------------------------")
print("Simple Calculator using if statement")

A = int (input("Enter first number: "))
B = int (input("Enter second number: "))

symbol_options = input("choose the operation you want to perform (+, -, *, /): ")

if B == float('inf') or B == float('-inf'):
    print("Error: Division by infinity is not allowed.")
elif A == float('inf') or A == float('-inf'):
    print("Error: Division by infinity is not allowed.")
    if symbol_options == "+":
        print("The sum of the two numbers is: ", A + B)
    elif symbol_options == "-":
        print("The difference of the two numbers is: ", A - B)
    elif symbol_options == "*":
        print("The product of the two numbers is: ", A * B)
    elif symbol_options == "/":
        print("The quotient of the two numbers is: ", A / B)
        if B == 0:
            print("Error: Division by zero is not allowed.")
        
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")    

