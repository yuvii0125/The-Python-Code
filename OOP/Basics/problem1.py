#Create student class that can take name and marks as arguments in constructor 
# Then create a method to print the average of marks

class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Average of marks is",sum/len(self.marks))

s1 = Student("Yuvraj", [50,60,70])
s1.average()
