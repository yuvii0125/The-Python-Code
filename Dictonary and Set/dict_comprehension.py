# 1. Create a dictionary of squares of even numbers from 0 to 20
even_squares = {x: x**2 for x in range(21) if x % 2 == 0}
print("Even Squares Dictionary:")
print(even_squares)

# 2. Count the occurrences of each letter in a word using dictionary comprehension
word = "programming"
letter_count = {letter: word.count(letter) for letter in set(word)}
print("\nLetter Count Dictionary:")
print(letter_count)

# 3. Create a dictionary from a list of tuples (fruit, quantity)
fruit_pairs = [("apple", 2), ("banana", 3), ("orange", 5), ("grape", 4)]
fruit_dict = {fruit: quantity for fruit, quantity in fruit_pairs}
print("\nFruit Quantity Dictionary:")
print(fruit_dict)

# 4. Combine the above two dictionaries: Create a new dictionary that shows fruit quantities and a note for low stock
low_stock_threshold = 3
stock_dict = {fruit: (quantity, "Low Stock" if quantity < low_stock_threshold else "In Stock") for fruit, quantity in fruit_dict.items()}
print("\nStock Status Dictionary:")
print(stock_dict)

# 5. Create a dictionary that maps numbers to their cubes for odd numbers
odd_cubes = {x: x**3 for x in range(21) if x % 2 != 0}
print("\nOdd Cubes Dictionary:")
print(odd_cubes)
