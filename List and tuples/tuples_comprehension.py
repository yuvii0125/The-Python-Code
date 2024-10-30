# Tuple comprehension, as a standalone concept, technically does not exist in Python.
#  Instead, we use generator expressions to create similar structures. 

#Syntax : (expression for item in iterable if condition)

squares = (x**2 for x in range(5))
print(squares)  # Output: <generator object ...>

squares_tuple = tuple(squares)
print(squares_tuple)  # Output: (0, 1, 4, 9, 16)


numbers = [1, 2, 3, 4]
squares_tuple = tuple(x**2 for x in numbers)
print(squares_tuple)  # Output: (1, 4, 9, 16)


even_squares = tuple(x**2 for x in range(10) if x % 2 == 0)
print(even_squares)  # Output: (0, 4, 16, 36, 64)
