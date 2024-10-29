def my_function():
    local_var = "I am local"  # Local variable
    print(local_var)

my_function()  # Output: I am local
# print(local_var)  # This would raise a NameError because local_var is not defined outside the function.


global_var = "I am global"

def my_function():
    print(global_var)

my_function()  # Output: I am global
print(global_var)  # Output: I am global 

counter = 0

def increment():
    global counter #Using Global keyword to define global varible inside function 
    counter += 1

increment()
print(counter)  # Output: 1
