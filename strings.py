"""
    Author: Lori White
    Purpose: Showing how to use strings in python.
"""
# The String Data Type
myStr = "This is a String"
print(myStr, "\n", type(myStr))
print(myStr, "is of data type", type(myStr))
# String Concatenation
str1, str2 = "water", "fall"
str3 = str1 + str2
print(str3)
# Input String
name = input("What is your name? ")
print(name)
# Format Output String
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))
print(f"{name}, you like a {color} {animal}.")
# Exceptions
# print(name + 3)
"""
  Expected Output:
Traceback (most recent call last):
  File "c:\python-workspace\Python-Practice-1\strings.py", line 18, in <module>
    print(name + 3)
TypeError: can only concatenate str (not "int") to str
"""
print(name + str(3))