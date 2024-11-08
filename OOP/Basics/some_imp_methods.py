class Animal:
    """
    This is a base class for animals. It defines general properties
    and methods that can be extended by subclasses.
    """
    
    def __init__(self, name):
        """
        Initializes an animal with the given name.
        
        :param name: The name of the animal
        """
        self.name = name

    def speak(self):
        """
        Returns a sound made by the animal.
        """
        return f"{self.name} makes a sound"

    def move(self):
        """
        Returns movement description for the animal.
        """
        return f"{self.name} moves around"

def inspect_object(obj):
    """
    This method combines dir(), __dict__, __doc__, and help() to provide 
    a comprehensive inspection of an object, class, or method.
    """
    print("dir() Output:")
    print(dir(obj))
    print("\n__dict__ Output:")
    print(obj.__dict__)
    print("\n__doc__ Output:")
    print(obj.__doc__)
    print("\nhelp() Output:")
    help(obj)

# Testing the combined method with an Animal object
animal = Animal("Dog")
inspect_object(animal)
