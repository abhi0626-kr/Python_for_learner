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