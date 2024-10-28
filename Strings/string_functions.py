#Remember Strings are immutable whatever opeation you do , the main string remain same

a = '   hello , this is me yuvraj  '

#1 len() function - used to find the length of the string
print(len(a))

#2 upper() function - used to convert the string to uppercase
print(a.upper())

#3 lower() function - used to convert the string to lowercase   
print(a.lower())

#4 title() function - used to convert the first character of each word to uppercase
print(a.title())

#5 capitalize() function - used to convert the first character of the string to uppercase
print(a.capitalize())

#6 strip() function - used to remove white spaces from the beginning and end of the string
print(a.strip())

#7  lstrip() function - used to remove white spaces from the beginning of the string
print(a.lstrip())

#8 rstrip() function - used to remove white spaces from the end of the string
print(a.rstrip())

#9 replace() function - used to replace the old string with the new string
print(a.replace("yuvraj","yuvraj kumar"))

#10 split() function - used to split the string into list
print(a.split(","))

#11 join() function - used to join the list into string
print(" ".join(a.split(",")))

#12 count() function - used to count the number of times the string occurs in the string
print(a.count("yuvraj"))

#13 find() function - used to find the index of the string
print(a.find("yuvraj"))

#14 index() function - used to find the index of the string in the string
print(a.index("yuvraj"))

#15 isalnum() function - used to check if the string is alphanumeric
print(a.isalnum())  

#16 isalpha() function - used to check if the string is alphabetic
print(a.isalpha())

#17 isdigit() function - used to check if the string is digit
print(a.isdigit())

#18 islower() function - used to check if the string is lowercase
print(a.islower())  

#19 isupper() function - used to check if the string is uppercase
print(a.isupper())  

#20 istitle() function - used to check if the string is titlecase
print(a.istitle())

#21 isnumeric() function - used to check if the string is numeric
print(a.isnumeric())

#22 isdecimal() function - used to check if the string is decimal    
print(a.isdecimal())    

#23 isspace() function - used to check if the string is whitespace
print(a.isspace())

#24 startswith() function - used to check if the string starts with the specified string
print(a.startswith("h"))

#25 endswith() function - used to check if the string ends with the specified string
print(a.endswith("j"))
