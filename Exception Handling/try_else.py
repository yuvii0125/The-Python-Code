try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e) 

#else executed when try successfully executed

else:
    print("I am inside else")