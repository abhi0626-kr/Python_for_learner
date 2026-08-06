
# #While loop
# #While loop is used to run the statement or group of statement or block of code until given the condition is true or satisfied.

x  = 10
while x > 5:
    print(x)
    x -= 1  # If we wasn't set a decrement or increment value it will run infinite time, 
            # So we have to set a incerment or decrement value to stop the loop after a certain condition is met.

i = 0 
while i < 10:
    print(i)
    i += 1  # If we wasn't set a decrement or increment value it will run infinite time, 
            # So we have to set a incerment or decrement value to stop the loop after a certain condition is met.

y = 5
while y >= 0:
    x = input("Enter a number: ")
    print(x)

#Break statement in while loop

i = 0
while i<=10:
    
    if i == 5:
        i += 1 
        break # If we use break statement it will stop the loop when the condition is met.
    print(i)


#Continue statement in while loop

i = 0
while i<=10:
    
    if i == 5:
        i += 1 #
        continue # If we use continue statement it will skip the current iteration and move to the next iteration.
    print(i)
    i += 1



x = 'python'
while 'p' in x:
    print(x)


#while statement using True
# The True () fun
x = 0 
while True:
    input("This will run infinite times unless broken.")
    x += 1
    print(x)
    if x >= 10:
        break

