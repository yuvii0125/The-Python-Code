no = int(input("Enter the number:"))

if no > 0:
    if no == 1:
        print("Number is not prime")
    elif no == 2:
        print("Number is prime")
    else:
        for i in range(2, no):
            if no % i == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")
else:
    print("Number is 0 which is not prime")