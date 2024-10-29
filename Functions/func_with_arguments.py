def goodDay(name, ending="Have a nice day"):
    print("Good Day, " + name)
    print(ending)
    return "ok"  
#Here we are passing 2 arguments
#Here ending is default argument so if we don't pass any value it will take "Have a nice day"
a = goodDay("Harry", "Thank you") 
print(a)

goodDay("Yuvraj")
goodDay("Yash" , "Happy New Year") 