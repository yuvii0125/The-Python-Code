#we have to open a file to read or write or perform any operation

# f = open("test.txt", "mode") r for read w for write  #default mode is read mode in python 

f = open("data.txt", "r")
'''
'r' = read mode (default)
'w' = write mode (delete all data and write new data)
'x' = create a file and open it for writing
'a' = append mode (means we do not delete data and add new data)
't' = text mode (default)
'b' = binary mode
'+' = read and write
'''
# data = f.read()  #If we do read(5) it will read first 5 characters 
# print(data)  #here if we do first read and then readline so readline will do not read anything
line1 = f.readline() #it will read first line
print(line1)
line2 = f.readline() #it will read second line
print(line2)
# print(type(data))
f.close()
