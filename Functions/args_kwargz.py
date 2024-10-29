def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

# Calling the function with different numbers of arguments
print(sum_numbers(1, 2))          # Output: 3
print(sum_numbers(1, 2, 3, 4, 5)) # Output: 15


def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
print_person_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

def display_info(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with both types of arguments
display_info(1, 2, 3, name="Bob", age=25)
# Output:
# Positional arguments:
# 1
# 2
# 3
#
# Keyword arguments:
# name: Bob
# age: 25

