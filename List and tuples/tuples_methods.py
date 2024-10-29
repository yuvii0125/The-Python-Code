# Creating a tuple with mixed data types
my_tuple = (1, 2, 3, 4, 2, 5, "hello", 2)

# 1. Accessing elements
print("Original Tuple:", my_tuple)

# Accessing the first and last element
print("First Element:", my_tuple[0])    # Output: 1
print("Last Element:", my_tuple[-1])     # Output: 2

# 2. Length of the tuple
print("Length of Tuple:", len(my_tuple))  # Output: 8

# 3. Slicing the tuple
sliced_tuple = my_tuple[2:5]
print("Sliced Tuple (index 2 to 4):", sliced_tuple)  # Output: (3, 4, 2)

# 4. Using the count() method
count_of_2 = my_tuple.count(2)  # Count occurrences of the value 2
print("Count of 2 in Tuple:", count_of_2)  # Output: 3

# 5. Using the index() method
index_of_3 = my_tuple.index(3)  # Find the index of the first occurrence of 3
print("Index of 3 in Tuple:", index_of_3)  # Output: 2

# 6. Using the index() method for a value that is not present
try:
    index_of_10 = my_tuple.index(10)  # This will raise a ValueError
except ValueError:
    print("10 is not in the tuple.")

# 7. Demonstrating immutability
# Trying to change an element (will raise an error)
try:
    my_tuple[0] = 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# Final output of the tuple
print("Final Tuple (unchanged):", my_tuple)  # Output: (1, 2, 3, 4, 2, 5, "hello", 2)

