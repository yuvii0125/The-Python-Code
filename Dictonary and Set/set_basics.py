e = {1,2,3,4 , 6 ,7,8,7,2}

s = set() #Never us s = {} for empty set as it is an empty dictionary
print(type(e))
print(type(s))

#sets are always unordered and unindexed

print(e) #{1, 2, 3, 4, 6, 7, 8} or {1, 2, 3, 4, 7,8,6} can be anything 
#set do not repeat values
#sets are mutable
# Sets can contain immutable (hashable) data types. Common immutable types include:
# Numbers: int, float, etc.
# Strings: e.g., "hello"
# Tuples: e.g., (1, 2)
# Frozensets: e.g., frozenset([1, 2, 3])