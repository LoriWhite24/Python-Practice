"""
    Author: Lori White
    Purpose: Showing how to use generators in python.
    Notes: Generators - are special functions that make iteration and memory management easier.
        "yield x" - Makes a function become a generator by returning a value while maintaining its position in the function.
        "next()" - used to navigate to the next value yielded in an instanced generator
"""
# Example of a Generator
def generateSeq():
    number = 0
    add = 1
    while True:
        yield number
        number += add
        add += number

seq = generateSeq()
for iteration in range(0, 10):
    print(f"Iteration {iteration}: {next(seq)}")