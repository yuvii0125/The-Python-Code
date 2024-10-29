# A tuple is an immutable sequence type that can hold a collection of items.
# Once a tuple is created, you cannot modify its content (add, remove, or change elements).
#tuples are indexed , starts with 0
#and like strings tuples are also have negative indexing
#where the last item index is -1 and the first item index is -len(tuple)


a = (1,45,342,3424,False, "Rohan", "Shivam")
print(a[-1]) 
print(a[-2])
print(type(a))
print(a[-len(a)])


#tuples do have slicing as well 
# Slicing a tuple
mixed_tuple = (1, "hello", 3.14, [4, 5], (6, 7))
#accessing elements through slicing where the first index is inclusive and the second index is exclusive
sliced_tuple = mixed_tuple[1:4]  # Output: ('hello', 3.14, [4, 5])
print(sliced_tuple)

# You can pack multiple values into a tuple and unpack them back into variables.
#packing 
packed_tuple = (1, 2, 3)

# Unpacking:
a, b, c = packed_tuple
print(a, b, c)  # Output: 1 2 3
