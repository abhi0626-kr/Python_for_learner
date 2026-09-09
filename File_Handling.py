# File Handling.
# File handling is an important aspect of programming that allows you to read, write, and manipulate files on your computer.
# In Python, you can work with files using built-in functions and methods.

#   Files Modes:
#       1. 'r' - Read mode (default): Opens a file for reading.
#               If the file does not exist, it raises a FileNotFoundError.

#       2. 'w' - Write mode: Opens a file for writing. If the file already exists,
#               it truncates the file to zero length. If the file does not exist, it creates a new file.

#       3. 'a' - Append mode: Opens a file for appending. If the file does not exist, 
#               it creates a new file.

#       4. 'r+' - update mode: Opens a file for updating. 
#               If the file does not exist, it raises a FileNotFoundError.


#       5. 'x' - create mode: Opens a file for creating a new file. 
#               If the file already exists, it raises a FileExistsError.



# Syntax for file handling:
file = open("filename.ext", "mode")  # mode can be 'r', 'w', 'a', 'x', or 'c'
file.close()  # close the file after use to free up system resources.

# Try to use the 'Exception handling' concept in 'file handling'.

# Example: Handling the case where a file already exists.
try:
    file = open("example.txt", "x")  # Attempt to open a file in create mode
except FileExistsError:
    print("Error: The file 'example.txt' already exists.")
    print("Please choose a different filename or delete the existing file.")
else:
    print("File 'example.txt' created successfully.")
    file.close()


paragraph = """File handling is an important aspect of programming that allows you to read, write, and manipulate files on your computer.

In Python, you can work with files using built-in functions and methods.It provides a way to store and retrieve data, making it possible to persist information between program executions. 

And using file handling, you can create, read, update, and delete files, as well as perform various operations on their contents.
"""

# Example:  write mode.
file = open("example.txt", "w")  # Open a file in write mode
file.write(paragraph)  # Write some content to the file
file.close()  # Close the file after use.

# Example:  read mode.
try:
    file = open("example.txt", "r")  # Open a file in read mode
    content = file.read()  # Read the content of the file
    print(content)  # Print the content to the console
    file.close()  # Close the file after use.
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
    print("Please create the file first.")

# Type of Read Methods:
# 1. read(): Reads the entire content of the file as a single string.
# 2. readline(): Reads a single line from the file.
# 3. readlines(): Reads all lines from the file and returns them as a list.



# Example:  readline mode.
try:
    file = open("example.txt", "r")  # Open a file in read mode
    content = file.readline()  # Read the content of the file
    print(content)  # Print the content to the console
    file.close()  # Close the file after use.
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
    print("Please create the file first.")



# Example:  readlines mode.
try:
    file = open("example.txt", "r")  # Open a file in read mode
    content = file.readlines()  # Read the content of the file
    print(content)  # Print the content to the console
    file.close()  # Close the file after use.
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
    print("Please create the file first.")


# Update mode:
# Example:  update mode.
File_Name = "example.txt"
try:
    file = open("example.txt", "r")  # Open a file in update mode
    Content = file.readlines()  # Read all lines from the file
    file.close()  # Close the file after use.
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
    print("Please create the file first.")
else :
    for i in Content:
        i = i.replace("/n", "")
        i = i.replace(".", "./n")
        for j in range(1, 100):
            if f"[{j}]" in i:
                i = i.replace(f"[{j}]","." )
        print(i)

        
# Delete mode:
# Example:  delete mode.

# We have to use the 'os' module to delete a file in Python. 

import os

File = "WpSystem"
path = "A:/"
print(File +" " + path)
File_Name = (File +" " + path)

try:
    if os.path.exists(File + path):
        os.remove(File + path)  # Delete the file
        print(f"File '{File_Name}' has been deleted.")
    else:
        print(f"Error: The file '{File_Name}' does not exist.")
        print("Please create the file first.")
except FileNotFoundError:
    print(f"Error: The file '{File_Name}' does not exist.")
    print("Please create the file first.")