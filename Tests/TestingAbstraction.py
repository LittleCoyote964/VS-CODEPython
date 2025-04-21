from abc import ABC, abstractmethod

# Define an abstract base class that sets a template for animals.
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Produce the sound associated with the animal."""
        pass

# Concrete subclass for Dog that implements the abstract method.
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

# Concrete subclass for Cat that implements the abstract method.
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Client code that uses the abstract interface.
def animal_sound(animal: Animal):
    print(animal.make_sound())

# Using the abstraction:
dog = Dog()
cat = Cat()

animal_sound(dog)  # Outputs: Bark!
animal_sound(cat)  # Outputs: Meow!