"""
    Author: Lori White
    Purpose: Showing how to use Static Debugging in python.
"""
# Python program with 2 errors
VAR = "Double Value"
sumValue = VAR + 4 # Expected Output: TypeError: can only concatenate str (not "int") to str

def dosomething(valuetocheck):
    """
     Checks a value.
    """
    if valuetocheck > 4:
        print("Bad indent")
        # Try playing with the indention and see what happens!
        # Static Analysis at work!
