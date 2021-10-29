"""
    Author: Lori White
    Purpose: Showing how to use polymorphism in python.
    Notes: Inheritance - is the process by which objects gain the properties of other objects.
        Parent class -  the type object, and it contains base information that all of its children inherit.
        Child class - the type created by the parent class and expands upon the information of that class.
        Overriding - Children can overwrite the inherited properties of their parent, changing the functionality.
        Can inherit from multiple parent classes.
"""
# Example of Inheritance
class mammal:
    """
     This represents a mammal.
    """
    circulation = "is warm blooded"
    skeleton = "is a vertebrate"
    skin = "has hair"
    parent = "produces milk"

class bird:
    """
     This represents a bird.
    """
    circulation = "is warm blooded"
    skeleton = "is a vertebrate"
    skin = "has feathers"
    parent = "lays eggs"

class humman(mammal):
    """
     This represents a human.
    """
    def __init__(self, myName):
        """
         Intializes the human.
        """
        self.myName = myName

class crow(bird):
    """
     This represents a crow.
    """
    def __init__(self, myName):
        """
         Intializes the crow.
        """
        self.myName = myName

class birdman(bird, humman):
    """
     This represents a birdman.
    """
    skin = humman.skin + " and " + bird.skin
    parent = humman.parent + " and " + bird.parent

frank = humman("Frank")
print(frank.myName + " " + frank.circulation)
print(frank.myName + " " + frank.skin)

alice = birdman("Alice")
print(alice.myName + " " + alice.parent)
print(alice.myName + " " + alice.skin)

greg = crow("Greg")
queue = [frank, alice, greg]
for animal in queue:
    if isinstance(animal, mammal):
        print(animal.myName + ", who " + animal.skin + ", is standing in line.")
    elif isinstance(animal, bird):
        print(animal.myName + ", who " + animal.skin + ", is flapping around.")