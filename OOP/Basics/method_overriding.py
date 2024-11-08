# Parent class for method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class that overrides the sound method
class Dog(Animal):
    def sound(self):  # Method overriding
        print("Dog barks")

# Method overloading with default arguments
class Calculator:
    # Overloaded method (using default arguments)
    def add(self, a, b=0, c=0):
        return a + b + c

# Testing method overriding and overloading
# Method overriding
animal = Animal()
animal.sound()  # Outputs: Animal makes a sound

dog = Dog()
dog.sound()  # Outputs: Dog barks

# Method overloading
calc = Calculator()
print(calc.add(10))  # Outputs: 10 (a + b + c where b and c are default 0)
print(calc.add(10, 20))  # Outputs: 30 (a + b)
print(calc.add(10, 20, 30))  # Outputs: 60 (a + b + c)
