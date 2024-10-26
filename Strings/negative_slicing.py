name = "Yuvraj"


# FOr Yuvraj we can do this
# Y = '-6' , v = '-5' , u = '-4' , r = '-3' , a = '-2' , j = '-1'
# as in positive slicing the index starts from 0
#In negative slicing the index starts from -length and end with -1

#when slicing with a range like x[start:end], the last index (end) is not included.
#  However, when using x[start:] (with no end index specified), 
# Python takes all characters from the start index to the end of the string, 
# including the last character.

print(name[0:3])

print(name[-4: -1]) 
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5]) but here 5 is included
print(name[1:5])


#here [1: ] means from 1st index to end

#here [:4] means from 0th index to 4th index
 
#negative sliciing
