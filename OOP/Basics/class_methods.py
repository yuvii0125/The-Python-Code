class Person:
    name = "Anonymus"

    # def changeName(self,name):
    #     # self.name = name 
    #     #for changing class Attribute
    #     #Person.name = name
    #     self.__class__.name = name

    @classmethod
    def changeName(cls,name):
        cls.name = name
    


p1 = Person()
p1.changeName("Yuvraj")
print(p1.name)
print(Person.name)


#Property Decorator
