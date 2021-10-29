"""
    Author: Lori White
    Purpose: Showing how to use modules in python.
"""
# Playing with the built-in math module
import math
x = float(input("Enter a numeric value: "))
print(math.fabs(x),"\n", math.floor(x))

# Playing with the os module
import os
print(os.listdir())
os.mkdir("New_Folder")
print(os.listdir())
os.rmdir("New_Folder")
print(os.listdir())
print(os.getlogin())