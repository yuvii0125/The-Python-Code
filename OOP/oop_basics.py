#class is a entity 
#Object is instance of class 

#constructor is called when object is created

#The data stored inside the class is called attributes
class Student:

    #Default constructor
    def __init__(self):
        print("constructor called when object is created")
    
    #Parameterized constructor
    def __init__(self,Name,Marks=20):    #Constructor have one argument self(can be anything but generally self is used)
        
        self.name = Name
        self.marks = Marks
        print(f"constructor called when {self.name}  is created")

s1 = Student("Yuvraj")
print(s1.name , s1.marks)

#Constructor called every single time when object is created 

s2 = Student("Yash", 50)
print(s2.name,s2.marks)