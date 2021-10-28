"""
    Author: Lori White
    Purpose: Showing how to use lists, tuples and dictionaries in python.
"""
# Lists
myFruitList = ["apple", "orange", "banana", "cherry", "strawberry"]
print(myFruitList)
print(type(myFruitList))
print("The Fruits: ", myFruitList[0], ",", myFruitList[1], ",", myFruitList[2], ",", myFruitList[3], ",", myFruitList[4])
myFruitList[1] = "mango"
print(myFruitList)
# Tuples
myFinalAnswerTuple = ("apple", "orange", "banana")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print("The Fruits: ", myFinalAnswerTuple[0], ",", myFinalAnswerTuple[1], ",", myFinalAnswerTuple[2])
# Dictionaries
myFavoriteFruitDictionary = {
    "Adam" : "apple",
    "Ben" : "banana",
    "Penny" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Adam"])
print(myFavoriteFruitDictionary["Ben"])
print(myFavoriteFruitDictionary["Penny"])
for key, value in myFavoriteFruitDictionary.items():
    print(f"{key} likes {value}.")