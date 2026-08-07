
# Game

from logging import warning
import random
from tkinter import W


print("Before starting the game please read the rules carefully.")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Rule 1: You only enter the number between 1 to 250 for 10 times.")
print("Rule 2: if you enter a number greater than 250 or less than 1 it will ask to enter the number again for 5 times with warning.")
print("Rule 3: Developer kept some numbers as Boom... if the user(You) enters those number you lost the game")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

x = 1 
Warning = 5

mines = [ 10, 20 ,30 ,55, 66, 143, 189, 199, 234, 250,]
while True:
    
     n = int(input(f"{x} Enter a number between 1 and 250: "))
     if n >= 1 and n <= 250:
      print("You entered a", x ,"correct number.")
     else:    
      print("You entered a", n ,"wrong number.")
      Warning -= 1
      if Warning == 0:
        print("You have entered the wrong number 5 times. Game over.")
        break
     #  if x >= 11:
     if n > 250 or n < 1:
          print("You have entered the wrong number", Warning, "times. Game over.")
          if Warning == 5:
           break
          else:
           continue
    #  if n == mines:    
     if n == 10 or n == 20 or n == 30:
       print("You lost the game.")
       break
      

     x += 1
     if x >= 11:
      break


        