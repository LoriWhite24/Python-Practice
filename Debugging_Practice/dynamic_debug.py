"""
    Author: Lori White
    Purpose: Showing how to use Dynamic Debugging in python.
"""
# Ask the user for a value and confirm the supplied value is greater than 0
def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int or type(valuetocheck) is float), "You must enter a number."
    assert (valuetocheck > 0), "Value entered must be greater then 0."
    if valuetocheck > 4:
        print("Value is greater than 4.")
try:
    var = int(input("Enter a number greater then 0: "))
    try:
        checkvalue(var)
        # checkvalue("")
    except AssertionError as error:
        print(error)
except ValueError:
    print("You must enter a number.")
print("End of Program.")