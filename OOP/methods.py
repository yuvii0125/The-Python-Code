#Class has 2 things
#1. Attributes
#2. Methods

#Methods are functions that belongs to  objects


class Student:
    college_name = "LDRP ITR"
    
    def __init__(self, name, marks=50):  # Set default value for marks
        self.name = name
        self.marks = marks

    def welcome(self):
        print(f"Welcome dear {self.name} to {self.college_name}")

    def get_marks(self):
        return self.marks

# Creating an instance with only the name; marks will default to 50
s1 = Student("Yuvraj")
s1.welcome()

# Creating an instance with both name and marks
s2 = Student("Aman", 75)
s2.welcome()

print(s1.get_marks())