# Creating a dictionary with different types of keys and values
#Keys must be immutable (int, float, str, tuple) and unique.
# Values can be any type (int, float, str, list, dict, etc.).
# Dictionary with different types of keys: int, float, string, and tuple

my_dict = {
    1: "integer key",                # Integer key with a string value
    3.14: "float key",               # Float key with a string value
    "name": "Yuvraj",                # String key with a string value
    (1, 2): "tuple key"              # Tuple key with a string value
}

# Printing the initial dictionary
print("Initial Dictionary:")
print(my_dict)

# Adding new entries with various types of values
my_dict["age"] = 20                   # Adding an integer value
my_dict["height"] = 5.9               # Adding a float value
my_dict["hobbies"] = ["coding", "music"]  # Adding a list value
my_dict["address"] = {                # Adding a dictionary as a value
    "city": "Mumbai",
    "country": "India"
}

# Function to demonstrate storing a function as a value
def greet(name):
    return f"Hello, {name}!"

my_dict["greeting_function"] = greet  # Storing a function as a value

# Printing the updated dictionary
print("\nUpdated Dictionary:")
print(my_dict)

# Accessing values using different keys
print("\nAccessing Values:")
print("Value for key 'name':", my_dict["name"])  # Accessing a string value
print("Value for key 1:", my_dict[1])              # Accessing an integer key
print("Value for key 3.14:", my_dict[3.14])        # Accessing a float key
print("Value for key (1, 2):", my_dict[(1, 2)])    # Accessing a tuple key

# Calling the function stored in the dictionary
print("\nCalling the stored function:")
print(my_dict["greeting_function"]("Yuvraj"))  # Output: Hello, Yuvraj!

# Demonstrating the use of .get() method
print("\nUsing .get() method:")
print("Value for key 'age':", my_dict.get("age", "Not found"))  # Key exists
print("Value for key 'nonexistent_key':", my_dict.get("nonexistent_key", "Not found"))  # Key does not exist
