"""
    Author: Lori White
    Purpose: Showing how to use a conditional in python.
"""
userReply = int(input("How many bananas do you have? "))
# The if Statement
if userReply >= 5:
    print("You have a bunch of bananas.")
# The elif statement
elif userReply >= 1 and userReply <= 4:
    print("You have a small bunch of bananas.")
# The else Statement
else:
    print("You do not have any bananas.")


