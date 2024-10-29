#list are mutable
#list are ordered
#list are indexed
#list can contain duplicate value

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])



# Creating a list with multiple data types
mixed_list = [1, 3.14, "Hello", True, [5, 6], {"key": "value"}, (7, 8)]

# Accessing elements
print("Original List:", mixed_list)

# Accessing specific types
print("Integer:", mixed_list[0])          # Output: 1
print("Float:", mixed_list[1])             # Output: 3.14
print("String:", mixed_list[2])            # Output: Hello
print("Boolean:", mixed_list[3])           # Output: True
print("Nested List:", mixed_list[4])       # Output: [5, 6]
print("Dictionary:", mixed_list[5])        # Output: {'key': 'value'}
print("Tuple:", mixed_list[6])             # Output: (7, 8)
