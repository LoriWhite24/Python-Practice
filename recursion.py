"""
    Author: Lori White
    Purpose: Showing how to use recursion in python.
    Notes: Recursion - occurs when a function calls itself inside of itself.
        You must include some sort of condition which will change sufficiently to end the recursion, or the function will nevr end.
"""
# Example of recursion
def addChain(number, increment):
    if number <= 0:
        return 0
    else:
        return number + addChain(number - increment, increment)

print("Using recursion we are chaining 10 by incrementing by 2.\nResult: " + str(addChain(10, 2)))