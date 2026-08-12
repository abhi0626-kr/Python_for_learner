help ("keywords")
#FizzBuzz1 


print("FizzBuzz")
n = int(input("Enter the value of n : "))
for i in range(1, n):

        if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
        elif i % 3 == 0:
         print("Fizz")
        elif i % 5 == 0:
                print("Buzz")
else:
        print(i)


#write a promgram to find the n number is Armstrong number or not using for loop 




n = int(input("Enter the value of n : "))

        
power = len(str(n))
val = 0
for i in str(n):
                
                val += int(i) ** power

                if val == n:
                        print(n, "is an Armstrong number")
                else:
                        print(n, "is not an Armstrong number")
else:   
        print("Please enter a valid number")        



# Wirte  a program to find the n number is prime number or not using for loop

n = int(input("Enter the value of n : "))
if n > 1:
        for i in range(2, n):
                if (n % i) == 0:
                        print(n, "is not a prime number")
                        break
        else:
                print(n, "is a prime number")


#write a program to Add two numbers without '+' or "Sum" operator
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1 
        print("The sum of the two numbers is: ", a)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

C = a-(-b)
print("The sum of the two numbers is: ", C)


# Nutural number's , perfect number's, Armstrong number's, Neon number's

#write a program to find perfect number
n = int(input("Enter the value of n : "))
sum = 0
for i in range(1, n):
        if n % i == 0:
                print(i)
                sum += i
if sum == n:
        print(n, "is a perfect number")
else:
        print(n, "is not a perfect number")


# Fibonacci Series

fib_lst = [0,1]

n=10 

for i in range(n-2):
    val = fib_lst[-1] + fib_lst[-2]
    fib_lst.append(val)

print(fib_lst)