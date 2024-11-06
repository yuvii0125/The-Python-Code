#Three types of Inheritence

#Single Inheritence
#Multiple Inheritence
#Multilevel Inheritence

#Multiple Inheritence
class Car:
    @staticmethod
    def start():
        print("Car is started..")

    @staticmethod
    def stop():
        print("Car is stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):

    def __init__(self,type):
        self.type = type