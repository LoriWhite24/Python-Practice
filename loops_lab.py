"""
    Author: Lori White
    Purpose: To use loops to play a number guessing game and count to 10.
"""
# The while loop

# The game rules
print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")

# Imports the random module.
import random

# Generates a random Integer between 1 and 10.
number = random.randint(1,10)

# Initializes the needed variables for the game.
isGuessRight = False
numberGuesses = 0

# Runs the guessing game.
while not isGuessRight:
    guess = input("Guess a number between 1 and 10: ")
    numberGuesses += 1
    if int(guess) == number:
        print("You guessed {} with {} tries. That is right! You win!".format(guess, numberGuesses))
        isGuessRight = True
    elif int(guess) > number:
        print("You guessed {}, which is higher then the actual number. Sorry, that isn’t it. Try again.".format(guess))
    else:
        print("You guessed {}, which is lower then the actual number. Sorry, that isn’t it. Try again.".format(guess))

# The for loop
print("Let’s count to 10!")
for x in range(0, 11):
  print(x)