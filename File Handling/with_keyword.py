#we do not need to close the file when using the with keyword 
with open("data3.txt","r+") as f:
    f.write("Hello This is data3.txt file")

