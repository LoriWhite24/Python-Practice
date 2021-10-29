"""
    Author: Lori White
    Purpose: Showing how to use polymorphism in python.
    Notes: Polymorphism - is the utilization of the same function for many purposes.
        With Iheritance - A child class can take methods from its parent class and override parts of them.
        With Classes - Two different classes can use methods of the same name to produce different results.
        With Types - Mulitple methods can be created that take different types as arguements, allowing them to be in many situations.
"""
# Example of Polymorphism
class dog():
    """
     This represents a dog.
    """
    def __init__(self, name):
        """
         Intializes the dog.
        """
        self.name = name
    def speak(self):
        """
         Get's the sound of the dog.
        """
        return "Arf! Arf!"
    
class chihuahua(dog):
    """
     This represents a chihuahua.
    """
    def speak(self):
        """
         Get's the sound of the chihuahua.
        """
        return "Yip! Yip!"

class cat():
    """
     This represents a cat.
    """
    def __init__(self, name):
        """
         Intializes the cat.
        """
        self.name = name
    def speak(self):
        """
         Get's the sound of the cat.
        """
        return "Meow! Meow!"

def teach(animal):
    """
     Prints the animal and it's sound to the terminal.
    """
    print(animal.name + " makes the noise: " + animal.speak())

balto = dog("Balto")
spike = chihuahua("Spike")
sally = cat("Sally")

print(balto.speak(),"\n", spike.speak(), "\n", sally.speak())
teach(balto)
teach(spike)
teach(sally)