try:
    with open("file.txt", "r") as f:
        print("file.txt content:")
        print(f.read())

except FileNotFoundError:
    print("Error: file.txt not found")

try:
    with open("file2.txt", "r") as f2:
        print("file2.txt content:")
        print(f2.read())

except FileNotFoundError:
    print("Error: file2.txt not found")

try:
    with open("file3.txt", "r") as f3:
        print("file3.txt content:")
        print(f3.read())

except FileNotFoundError:
    print("Error: file3.txt not found")
