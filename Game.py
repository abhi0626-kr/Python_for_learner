
# Game
print("Before starting the game please read the rules carefully.")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Rule 1: You only enter the number between 1 to 250 for 10 times.")
print("Rule 2: if you enter a number greater than 250 or less than 1 it will ask to enter the number again for 5 times with warning.")
print("Rule 3: Developer kept some numbers as Boom... if the user(You) enters those number you lost the game")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

x = 1 
# num = int(input("Enter a number between 1 and 250: "))
while True:
     print(x)
     n = int(input("Enter a number between 1 and 250: "))
     if n > 1 or n < 250:
      print("You entered a", x ,"correct number.")
     else:    
      print("You entered a", x ,"wrong number. Please enter a number between 1 and 250.")
      break
     #  if x >= 11:
     if n > 250 or n < 1:
          print("You have entered the wrong number 5 times. Game over.")
          if x >= 5:
           break
     if n == 10 or n == 20 or n == 30:
       print("You lost the game.")
       break
      

     x += 1
    #  print(x)
     if x >= 11:
      break


# # x += 1
# # if x >= 5:
#         print("You have entered the wrong number 5 times. Game over.")
        

        
