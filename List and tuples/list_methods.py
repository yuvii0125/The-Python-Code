# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# 1. Accessing elements
print("First Element:", my_list[0])  # Output: 1
print("Last Element:", my_list[-1])   # Output: 5

# 2. Slicing
print("Slice from index 1 to 3:", my_list[1:4])  # Output: [2, 3, 4]

# 3. Length of a list
print("Length of the list:", len(my_list))  # Output: 5

# 4. Adding elements
my_list.append(6)  # Adds an element to the end of the list
print("After appending 6:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 5. Inserting elements
my_list.insert(2, 2.5)  # Inserts 2.5 at index 2
print("After inserting 2.5 at index 2:", my_list)  # Output: [1, 2, 2.5, 3, 4, 5, 6]

# 6. Removing elements
my_list.remove(2.5)  # Removes the first occurrence of 2.5
print("After removing 2.5:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 7. Popping elements
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped Element:", popped_element)  # Output: 6
print("After popping an element:", my_list)  # Output: [1, 2, 3, 4, 5]

# 8. Reversing the list
my_list.reverse()  # Reverses the list in place
print("Reversed List:", my_list)  # Output: [5, 4, 3, 2, 1]

# 9. Sorting the list
my_list.sort()  # Sorts the list in ascending order
print("Sorted List:", my_list)  # Output: [1, 2, 3, 4, 5]

# 10. Counting occurrences
count_of_2 = my_list.count(2)  # Counts occurrences of 2
print("Count of 2 in the list:", count_of_2)  # Output: 1

# 11. Finding the index of an element
index_of_3 = my_list.index(3)  # Finds the index of the first occurrence of 3
print("Index of 3 in the list:", index_of_3)  # Output: 2

# 12. Extending the list
another_list = [6, 7, 8]
my_list.extend(another_list)  # Adds elements of another_list to the end
print("After extending with [6, 7, 8]:", my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 13. Clearing the list
my_list.clear()  # Removes all elements from the list
print("After clearing the list:", my_list)  # Output: []
