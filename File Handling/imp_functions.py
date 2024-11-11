
#Seek Function : Changes the file's current position to a specified location.
file = open("example.txt", "r")
file.seek(10)  # Move to the 10th byte in the file
print(file.read())  # Read from the new position
file.close()

#Tell Function :  Returns the current position in the file as the number of bytes from the beginning
file = open("example.txt", "r")
print(file.tell())  # Outputs 0 (start of the file)
file.read(5)
print(file.tell())  # Outputs 5 (after reading 5 bytes)
file.close()

"""
# Open the file in read-write mode
file = open("example.txt", "r+")

# Truncate the file to 10 bytes from the beginning
file.truncate(10)


truncate means reduce the size of the file to 10 bytes from the beginning

# Check the size of the file after truncation
file.seek(0)
print(file.read())  # This will read the file up to 10 bytes

file.close()

"""