"""
    Author: Lori White
    Purpose: Showing that a list in python can have multiple data types stored within the same list.
"""
# Mixed Bag
myMixedBagList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
secList = [4, 8, False]
for item in myMixedBagList:
    print("{} is of data type {}".format(item, type(item)))
for value in secList:
    print("{} is of data type {}".format(value, type(value)))
