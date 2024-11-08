# print(1+2) #3
# print("Hello" + "New") #HelloNew
# print([1,2] + [3,4]) #[1, 2, 3, 4] 

#SO , Here 1 operator have multiple method with different data type its called operator overloading


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def ShowNumber(self):
        print(f"{self.real} + {self.img}i") 

    def __add__(self,num2):  #Dunder Functions 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self,num2):  #Dunder Functions 
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)


num1 = Complex(1,2)
num1.ShowNumber()


num2 = Complex(3,4)
num2.ShowNumber()

num3 =num1 + num2
num3.ShowNumber()

num4 = num3 - num1
num4.ShowNumber()