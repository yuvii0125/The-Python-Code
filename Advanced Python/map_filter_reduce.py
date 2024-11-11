from functools  import reduce
#Map applies a function to all the items in input list

l = [1,2,3,4,5]

sqList = list(map(lambda x : x*x , l)) #map function = {function , list}

print(sqList)

index = 1
for index,item in enumerate(sqList):
    print(f"the {item} is present at index {index}")
    index += 1



#Filter : 
#Filter creates a new list for which the function returns true

Even = lambda x : x%2 == 0

evenList = list(filter(Even , l)) #filter function = {function , list}
print(evenList)


#Reduce:

sum = reduce(lambda x,y : x+y , l) #reduce function = {function , list}
print(sum)
