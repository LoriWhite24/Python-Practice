"""
    Author: Lori White
    Purpose: Showing how to use a assignment operators and basic math in python.
"""
# Assignment Operators
myVar = 1
myVar = myVar + 2
print(myVar)
myVar = 1
myVar += 2
print(myVar)
# Basic Math Practice
x = 5
y = 8
z = x + y
print(x + y)
print(z)
print(f"{x} + {y} =", z)
# Adding ints and floats
j = 6
k = 10.9
print(j + k)
print(int(j + k)) # This is flooring
# Using BODMAS
print((x - 5) + y ** 2)