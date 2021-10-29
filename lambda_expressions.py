"""
    Author: Lori White
    Purpose: Showing how to use lambda expressions in python.
    Notes: Lambda Expressions - are functions that can be created on the spot without even being named.
        Consist of one expression and a return of the result.
        "lambda values : expression" - takes the values given and uses them to evaluate the expression, returning the result
        You may pass the lambda expression to a variable, which will allow you to access the function by that variable name at a later time.
"""
# Example of a Lambda Expression
def exponent(e):
    return lambda x : x ** e
square = exponent(2)
cube = exponent(3)
print(f"10^2 = {square(10)}")
print(f"10^3 = {cube(10)}")