list = [1, True, 45.6, 'hello'] 
# i = 0
# while(i < len(list)):
#     print(list[i])
#     i += 1
for i in range(len(list)): #Here we do not need to use i += 1
    print(list[i])  

for item in list:
    print(item)


#Tuples can be print used for loop

tuple = (1, True, 45.6, 'hello')

for item in tuple:
    print(item)

#Srtring can be print used for loop

string = "hello"   
for item in string: 
    print(item)
