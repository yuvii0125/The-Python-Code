#there are two types of loops
#1. for loop
#2. while loop

# for loop
#in for loop 
#for i in range(1,10) so it means start from 1 and less than 10
#for i in range(1,10,2) so it means start from 1 and less than 10 and increment by 2
#for i in range(1,10,-3) so it means start from 1 and less than 10 and decrement by 3


#range() function range(start,stop,step_size)


for i in range(10): #range(10) means 0,1,2,3,4,5,6,7,8,9  Here it mean range(0,10)
    print(i)

for i in range(1,11): #range(1,11) means 1,2,3,4,5,6,7,8,9,10
    print(i)

for i in range(1,11,2): #range(1,11,2) means 1,3,5,7,9 
    print(i)

for i in range(10,0,-1): #range(10,0,-1) means 10,9,8,7,6,5,4,3,2,1
    print(i)
    