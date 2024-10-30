#List comprehension used to create a new list from an existing list in concise way 
# syntax : [expression for item in iterable if condition]


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square = [x**2 for x in list if x%2 == 0] 
# print(square)

#If-else :
numbers = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)  # Output: ['odd', 'even', 'odd', 'even', 'odd']


#Nested Loops : 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
