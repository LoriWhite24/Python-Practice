"""
    Author: Lori White
    Purpose: To use conditionals to ask the user if they would like stamps, an envelope, or make a copy.
"""
# The if Statement
userReply = input("Do you need to ship a package? (Type yes or no) ")
if userReply.lower == "yes":
      print("We can help you ship that package!")
# The else Statement
else:
      print("Please come back when you do need to  ship a package. Thank you.")
# The elif statement
userReply = input("Would you like to buy stamps, an envelope, or make a copy? (Type stamps, envelope, or copy)")
if userReply == "stamps":
    print("We have plenty of stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Type a number)")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, please come again.")

# The switch statement

# The function for the stamp choice
def stamp():
    print("We have plenty of stamp designs to choose from.")
# The function for the envelope choice
def envelope():
    print("We have many envelope sizes to choose from.")
# The function for the copy choice
def copies():
    copies = input("How many copies would you like? (Type a number)")
    print("Here are {} copies".format(copies))
# The function for the default choice
def default():
    print("Thank you, please come again.")
# The function for the switch statement
def options(argument):
    switcher = {
        "stamps": stamp,
        "envelope": envelope,
        "copy": copies,
    }
    return switcher.get(argument, default)()

userReply = input("Would you like to buy stamps, an envelope, or make a copy? (Type stamps, envelope, or copy)")
options(userReply)