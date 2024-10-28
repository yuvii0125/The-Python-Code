# Initialize a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. Using dict.clear()
print("Original Dictionary:", my_dict)
my_dict.clear()
print("After clear():", my_dict)  # Output: {}

# Reinitialize the dictionary for the next methods
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 2. Using dict.copy()
new_dict = my_dict.copy()
print("Copied Dictionary:", new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. Using dict.get()
value = my_dict.get('b', 0)
print("Value of 'b':", value)  # Output: 2
value_not_found = my_dict.get('d', 0)
print("Value of 'd' (not found):", value_not_found)  # Output: 0

# 4. Using dict.items()
items = my_dict.items()
print("Items in the dictionary:", items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 5. Using dict.keys()
keys = my_dict.keys()
print("Keys in the dictionary:", keys)  # Output: dict_keys(['a', 'b', 'c'])

# 6. Using dict.pop()
popped_value = my_dict.pop('b', 'Not Found')
print("Popped value:", popped_value)  # Output: 2
print("After pop('b'):", my_dict)  # Output: {'a': 1, 'c': 3}

# 7. Using dict.popitem()
popped_item = my_dict.popitem()
print("Popped item:", popped_item)  # Output: ('c', 3) or ('a', 1) depending on the order
print("After popitem():", my_dict)  # Output: Remaining items

# 8. Using dict.update()
my_dict.update({'d': 4})  # Adding a new key-value pair if do not exist
print("After update():", my_dict)  # Output: {'a': 1, 'd': 4}

# 9. Using dict.setdefault()
default_value = my_dict.setdefault('e', 5)
print("Value of 'e' after setdefault():", default_value)  # Output: 5
print("After setdefault():", my_dict)  # Output: {'a': 1, 'd': 4, 'e': 5}

# 10. Using dict.values()
values = my_dict.values()
print("Values in the dictionary:", values)  # Output: dict_values([1, 4, 5])
