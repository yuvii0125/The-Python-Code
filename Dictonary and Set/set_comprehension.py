    # 1. Create a set of squares of numbers from 0 to 10
squares_set = {x**2 for x in range(11)}
print("Squares Set:")
print(squares_set)

# 2. Create a set of unique vowels from a given word
word = "exemplary"
unique_vowels = {char for char in word if char in 'aeiou'}
print("\nUnique Vowels Set:")
print(unique_vowels)

# 3. Create a set of even numbers from a list with duplicates
numbers_with_duplicates = [1, 2, 3, 2, 4, 4, 5, 6, 8, 10, 10]
even_numbers_set = {num for num in numbers_with_duplicates if num % 2 == 0}
print("\nEven Numbers Set (from duplicates):")
print(even_numbers_set)

# 4. Create a set of characters from a string (removing duplicates automatically)
input_string = "hello world"
unique_characters_set = {char for char in input_string}
print("\nUnique Characters Set:")
print(unique_characters_set)

# 5. Create a set of cubes of odd numbers from 0 to 10
odd_cubes_set = {x**3 for x in range(11) if x % 2 != 0}
print("\nCubes of Odd Numbers Set:")
print(odd_cubes_set)
