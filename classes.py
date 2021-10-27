"""
Class - collection of related functions and variables that act 
as a template for arranging different sets of data.
Need two parts:
1. Declaration - similar to the declaration of a function
2. Initialization - is function that is within the class and 
   is responsible for creating new members of it.
A class can have associated functions and variables that are
attached to the class and identified as properties of it.
"""
# Example of a Class
# Here is where we defined a fruit
class fruit:
    def __init__(self, name, color, shape, texture, insideC, insideT):
        self.name = name
        self.color = color
        self.shape = shape
        self.texture = texture
        self.insideColor = insideC
        self.insideTexture = insideT
    def aboutMe(self):
        print(f"I am a {self.name}, I am shaped like a {self.shape}, and I am {self.color}! If you touch me, I feel {self.texture}.")
    def peel(self):
        self.color = self.insideColor
        self.texture = self.insideTexture
# Here is where we create three fruit objects
myBanana = fruit("banana", "yellow", "crescent", "smooth", "white", "sticky")
myApple = fruit("apple", "red", "sphere", "smooth", "white", "porous")
myOrange = fruit("orange", "orange", "sphere", "rough", "yellow", "porous")
# Here is where we called the fruit functions on a fruit object myBanana
myBanana.aboutMe()
myBanana.peel()
myBanana.aboutMe()
# Here is where we retrieved the properties of our fruit objects myApple and myOrange
print(f"My apple is {myApple.color} on the outside and {myApple.insideColor} on the inside.")
print(f"My orange feels {myOrange.texture}, and my apple feels {myApple.texture}.")
# Here is where we changed a property of a fruit object myOrange
myOrange.color = "blue"
print(f"I painted my orange, and the color is now {myOrange.color}.") 

print(type(myApple))