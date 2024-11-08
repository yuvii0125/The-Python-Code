class Animal:
    def __init__(self, name, species):
        self.name = name  # Instance variable for the name
        self.species = species  # Instance variable for the species

    def sound(self):
        return "Some generic animal sound"

    def describe(self):
        # Calling super().__init__ to invoke the parent constructor
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the parent class constructor using super()
        super().__init__(name, species="Dog")
        self.breed = breed  # Additional attribute for breed

    def sound(self):
        # Overriding the sound method and using super() to call the parent class method
        parent_sound = super().sound()
        return f"{parent_sound} and barks"

    def describe(self):
        # Overriding the describe method
        parent_description = super().describe()
        return f"{parent_description}. Breed: {self.breed}"


# Testing the Dog class
dog = Dog(name="Buddy", breed="Golden Retriever")

print(dog.sound())       # Output: Some generic animal sound and barks
print(dog.describe())    # Output: Buddy is a Dog. Breed: Golden Retriever
