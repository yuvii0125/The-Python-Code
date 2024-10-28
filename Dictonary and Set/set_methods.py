# Creating a set
my_set = {1, 2, 3}
print("Initial set:", my_set)

# Adding elements
my_set.add(4)
print("After add(4):", my_set)

my_set.update([5, 6])
print("After update([5, 6]):", my_set)

# Removing elements
my_set.remove(2)
print("After remove(2):", my_set)

my_set.discard(10)  # No error
print("After discard(10):", my_set)

popped_element = my_set.pop()
print("After pop():", my_set, "Popped element:", popped_element)

# Clearing the set
my_set.clear()
print("After clear():", my_set)

# Re-creating the set for further operations
my_set = {1, 2, 3}
print("\nRe-created set:", my_set)

# Creating another set for operations
other_set = {2, 3, 4, 5}

# Set operations
union_set = my_set.union(other_set)
print("Union (my_set | other_set):", union_set)

intersection_set = my_set.intersection(other_set)
print("Intersection (my_set & other_set):", intersection_set)

difference_set = my_set.difference(other_set)
print("Difference (my_set - other_set):", difference_set)

symmetric_difference_set = my_set.symmetric_difference(other_set)
print("Symmetric Difference (my_set ^ other_set):", symmetric_difference_set)

# Copying the set
my_copy = my_set.copy()
print("Copied set:", my_copy)

# Checking subset and superset
print("Is {1} a subset of {1, 2, 3}?", {1}.issubset(my_set))
print("Is {1, 2, 3} a superset of {1}?", my_set.issuperset({1}))

# Updating the set with intersection, difference, and symmetric difference
my_set.intersection_update(other_set)
print("After intersection_update(other_set):", my_set)

my_set = {1, 2, 3}  # Re-creating the set for demonstration
my_set.difference_update(other_set)
print("After difference_update(other_set):", my_set)

my_set.symmetric_difference_update(other_set)
print("After symmetric_difference_update(other_set):", my_set)
