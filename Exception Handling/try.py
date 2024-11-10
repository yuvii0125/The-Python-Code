# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)

# except ZeroDivisionError:
#     print("You cannot divide by zero")



try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
