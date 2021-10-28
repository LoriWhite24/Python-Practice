"""
    Author: Lori White
    Purpose: To show how a string is a list of characters.
"""
oldString = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print(oldString)
# Reads the string by one character at a time.
for i in range(0, len(oldString)):
    print(i, oldString[i])
# Takes a substring from the old string that consists of the first 24 characters.
newString = oldString[0:24]
print(newString)