#Control Statement
#Type of control statements.
 #pass
 #Break
 #continue

#Break Statement.
M = int(input("Enter the i value : "))

for i in range(M):
    if i == 60:
        break
    print(i)

# continue Statement
N = int(input("Enter the i value : "))

for i in range(N):
    if i == 60:
        continue
    print(i)

# Pass Statement
O = int(input("Enter the i value : "))

for i in range(O):
    if i == 60:
        pass
    print(i)

    
#write a program to print the numbers Sum of n numbers. eg N = 3 it will show 1+2+3 = 6
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of numbers from 1 to", n, "is :", sum)

#Write a program to calculate the factorial of a number using for loop.
n = int(input("Enter the value of n : "))
factorial = 1
for i in range(1, n + 1):   
    factorial *= i
print("Factorial of", n, "is :", factorial)