"""
    Author: Lori White
    Purpose: Showing how to use loops in python.
"""
counter = 0
# The while loop
while counter <= 3:
    print(counter)
    counter += 1
print("Final value for counter: ", counter)

# This is not a good practice, using while True
while True:
    if counter > 3:
        print("The while loop was ran.")
        break
    else:
        print(counter)
        counter += 1

# The for loop
myCars = ["Toyota", "Tesla", "Ford", "BMW", "Jeep", "Kia", "Honda"]
cars = ""
for car in myCars:
    cars += car + " "
print(cars)

for index in range(0, len(myCars)):
    print(index, ": " + myCars[index])

number = 3
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}! = {factorial}")

gameBoard = [["X", "O", "X"], [" ", "X", " "], [" ", " ", "O"]]
output = ""
for j in range(0, len(gameBoard)):
    for i in range(0, len(gameBoard[j])):
        if i == len(gameBoard[j]) - 1:
            output += gameBoard[j][i]
        else:
            output += gameBoard[j][i] + " | "
    if j < len(gameBoard) - 1:
        output += "\n----------\n"
print(output)