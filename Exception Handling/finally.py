"""
In Python, the finally keyword is used in a try-except block to ensure that certain code executes no matter 
what happens in the preceding try and except blocks. This is useful for cleanup actions, like closing files, releasing resources, 
or any other operations that should be performed after a block of code runs, regardless of whether an exception occurred.
"""

# try:
#     # Code that may raise an exception
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Division by zero!")
# finally:
#     print("This will always execute.")



def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    finally:
        print("Execution complete. Cleaning up resources if any.")

# Testing the function
print("Test 1:")
divide_numbers(10, 2)   # Should work normally
print("\nTest 2:")
divide_numbers(10, 0)   # Should trigger ZeroDivisionError
