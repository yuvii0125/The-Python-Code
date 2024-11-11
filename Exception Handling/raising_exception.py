a = int(input("Enter a first number: ")) 
b = int(input("Enter a second  number: ")) 


if(b==0):
    raise ZeroDivisionError("You cannot divide by zero")
else:
    print(a/b)