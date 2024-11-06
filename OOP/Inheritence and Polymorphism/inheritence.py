#When one class (child / derived) derives the properties and methods of another class(parents/base)
class Car:
    @staticmethod
    def start():
        print("Car is started..")

    @staticmethod
    def stop():
        print("Car is stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("INNOVA")
car2 = ToyotaCar("FORTUNER")

print(car1.start())