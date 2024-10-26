#strings do have 2 types of slicing
#1.using positive slicing
#2.using negative slicing

a = 'hello world'
print(a[0:5])

# here we are starting from 0th index and ending at 5th index but 5th index is not included 

#indexing start from 0 , 0 means 1 character and space is also known as character

b = "Python"
print(b[0])
#it gives only one output

c = "Python"
print(c[0:3:2])

#here we are starting from 0th index and ending at 3rd index but 3rd index is not included

#here we are skipping 2 characters

d = "Python"    
print(d[::2])    

#here we are skipping 2 characters and starting from 0th index and ending at end of string

e = "Python"
print(e[:])
