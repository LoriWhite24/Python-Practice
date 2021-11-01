"""
    Author: Lori White
    Purpose: Showing how to use the json module in python.
"""
import json
filename = 'Data_Files/userName.json'
name = input("What is your name? ")
users = []
# Check for a history file
try:
    with open(filename, "r") as reader:
        # Load the user's name from the history file
        users = json.load(reader)
except IOError:
    print("Could not load JSON file")

def found_name():
    """
     Searches the users for if the user exists.
    """
    found = False
    for user in users:
        if user["name"] == name:
            found = True
            break
    return found

# If the user was found in the history file, welcome them back
if found_name():
    print("Welcome back, " + name + "!")
else:
    # If they do not exist in the history file, ask the user for their age
    print("Welcome, " + name + "!")
    age = int(input("Since it's your first time logging in, what is your age? "))
    newUser = {}
    newUser["name"] = name
    newUser["age"] = age
    users.append(newUser)
    with open(filename, "w") as writer:
        writer.write(json.dumps(users))
