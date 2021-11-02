"""
    Author: Lori White
    Purpose: Showing how to use Static Debugging in python.
"""
# Python program with 2 errors
var = "Double Value"
sumValue = var + 4 # Expected Output: TypeError: can only concatenate str (not "int") to str

def dosomething(valuetocheck):
    if valuetocheck > 4:
        print("Bad indent") # Try playing with the indention and see what happens! Static Analysis at work!