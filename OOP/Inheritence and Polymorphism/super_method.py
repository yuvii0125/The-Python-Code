# This class defines the blueprint for a generic car
class Car:
    def __init__(self, type):
        # Initialize the car's type attribute
        self.type = type

    @staticmethod
    def start():
        # Static method to simulate starting a car (common functionality)
        print("Car is started..")

    @staticmethod
    def stop():
        # Static method to simulate stopping a car (common functionality)
        print("Car is stopped..")

# This class inherits from the Car class to represent a specific Toyota car
class ToyotaCar(Car):
    def __init__(self, name, type):
        # Initialize the ToyotaCar's name attribute
        self.name = name

        # Call the parent class __init__ method using super() to initialize the type attribute
        super().__init__(type)

# Create an instance of ToyotaCar
car1 = ToyotaCar("prius", "sedan")

# Print the car type
print(car1.type)