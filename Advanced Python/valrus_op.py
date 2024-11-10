# Without walrus operator
# line = input("Enter text: ")
# while line != "quit":
#     print(f"You entered: {line}")
#     line = input("Enter text: ")

# With walrus operator
while (line := input("Enter text: ")) != "quit":
    print(f"You entered: {line}")

'''
# Without walrus operator
values = [len(x) for x in data if len(x) > 2]

# With walrus operator
values = [n for x in data if (n := len(x)) > 2]

'''