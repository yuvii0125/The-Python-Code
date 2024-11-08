class Student:

    def __init__(self, phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths )/ 3 ) + "%"
    
stu1 = Student(80, 70, 90)
print(stu1.percentage)

#Now we found that we have to change the 1 subject marks and then we have to find percentage for stu1 
#SO , still stu1 pecentage is 80%

stu1.phy = 85
print(stu1.phy)
print(stu1.percentage)
