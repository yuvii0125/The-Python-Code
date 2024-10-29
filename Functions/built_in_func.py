# Importing required library
import math

# 1. print()
print("Demonstration of Important Built-in Functions")

# 2. len()
my_list = [1, 2, 3, 4, 5]
print(f"Length of my_list: {len(my_list)}")

# 3. type()
my_variable = 3.14
print(f"Type of my_variable: {type(my_variable)}")

# 4. int(), float(), str()
num_str = "42"
num_float = "3.14"
print(f"String to integer: {int(num_str)}")      # Converts string to integer
print(f"String to float: {float(num_float)}")    # Converts string to float
print(f"Integer to string: {str(100)}")           # Converts integer to string

# 5. max(), min()
numbers = [10, 20, 5, 30, 15]
print(f"Maximum number: {max(numbers)}")
print(f"Minimum number: {min(numbers)}")

# 6. sum()
print(f"Sum of numbers: {sum(numbers)}")

# 7. sorted()
unsorted_list = [3, 1, 4, 1, 5, 9, 2]
print(f"Sorted list: {sorted(unsorted_list)}")

# 8. range()
print("Numbers from range:")
for i in range(5):
    print(i, end=' ')
print()  # New line

# 9. enumerate()
print("Enumerated list:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# 10. zip()
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print("Zipped lists:")
for item in zip(list1, list2):
    print(item)

# 11. any(), all()
truth_values = [False, True, False]
print(f"Any True in truth_values: {any(truth_values)}")
print(f"All True in truth_values: {all(truth_values)}")

# 12. math functions
print(f"Square root of 16: {math.sqrt(16)}")  # Using a math function

# 13. Reversing a string using built-in functions
my_string = "Hello, World!"
reversed_string = ''.join(reversed(my_string))
print(f"Reversed string: {reversed_string}")

# 14. Using str.upper() and str.lower()
print(f"Uppercase: {my_string.upper()}")
print(f"Lowercase: {my_string.lower()}")

# 15. Using list comprehension with built-in functions
squared_numbers = [x**2 for x in range(1, 6)]
print(f"Squared numbers: {squared_numbers}")

# 16. Using filter() and map()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers from list: {even_numbers}")

squared_numbers_map = list(map(lambda x: x**2, numbers))
print(f"Squared numbers using map: {squared_numbers_map}")
