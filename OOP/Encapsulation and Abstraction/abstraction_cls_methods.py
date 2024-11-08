from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # No implementation here

    @abstractmethod
    def move(self):
        pass  # No implementation here

# Subclass of Animal that implements the abstract methods
class Dog(Animal):
    def sound(self):
        print("Dog barks")

    def move(self):
        print("Dog runs")

# Subclass of Animal that implements the abstract methods
class Bird(Animal):
    def sound(self):
        print("Bird chirps")

    def move(self):
        print("Bird flies")

# Uncommenting the next line will raise an error because Animal is abstract
# animal = Animal()

# Creating objects of subclasses
dog = Dog()
dog.sound()  # Output: Dog barks
dog.move()   # Output: Dog runs

bird = Bird()
bird.sound()  # Output: Bird chirps
bird.move()   # Output: Bird flies
