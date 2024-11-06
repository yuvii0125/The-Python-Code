# Defining a class named 'Person'

#Private Attributes and methods are meant to be used only within the class
#And are not meant to be accessed from outside the class

class Person:
    # Private class attribute '__name' with a default value "Anonymus"
    __name = "Anonymus"

    # Private method '__hello' that prints a greeting message
    def __hello(self):
        # This method prints "Hello, my name is" followed by the private attribute '__name'
        print("Hello, my name is", self.__name)

    # Public method 'welcome' that calls the private '__hello' method
    def welcome(self):
        # Accessing the private method '__hello' from within the class
        self.__hello()

# Creating an instance of the Person class
p1 = Person()

# Calling the public 'welcome' method, which in turn calls the private '__hello' method
p1.welcome()
