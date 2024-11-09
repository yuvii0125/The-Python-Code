 #There are 2 ways of writing to a file

#If we give a name of file in open which do not exist then python will create a new file

#1st way using 'w' mode where all the data will be overwritten
#2nd way using 'a' mode where all the data will be appended (means added after)

f = open("data1.txt", "w")
f.write("I am learning python now")
f.close()


f = open("data1.txt", "a")
f.write("\nNext I have to learn pandas and numpy")
f.close()

#If we open a file in r+ mode so it will read and write both and data will entered at start of file

f = open("data2.txt", "r+")
f.write("Next I have to learn Matplotlib and Seaborn")
f.close() 


#If we open a file in w+ mode so it will truncate  then write  and read both and data will entered at start of file

#If we open a file in a+ mode so it will append  then write  and read both and data will entered at end of file