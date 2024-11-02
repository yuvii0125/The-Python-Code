#2 Types of Attributes
#Class Attributes (Static Attributes)
#Object Attributes (Instance Attributes)


class Car:

    #Class Attributes
    wheels = 4 #This will be the same for the all objects and declaring here means it occupes
                  #only memory once
    color = "black" #defalut attribute
    #Instance Attributes
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

#if object and class attribute both have same name then object attributes are prioritized

c1 = Car("Black", 200)
c2 = Car("Red", 220)

print(c1.color, c1.speed, c1.wheels)
print(c2.color, c2.speed, c2.wheels)

#if i want to access wheel
print(Car.wheels)

#but i want to access color , speed i can do it with
print(c1.color, c1.speed)