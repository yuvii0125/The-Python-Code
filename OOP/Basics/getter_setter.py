class Person:
    def __init__(self, name):
        self._name = name  # Private attribute with a leading underscore

    # Getter for name attribute
    @property
    def name(self):
        """Getter method to access the private attribute _name."""
        return self._name

    # Setter for name attribute
    @name.setter
    def name(self, new_name):
        """Setter method to update the private attribute _name."""
        if isinstance(new_name, str) and new_name.strip():  # Validation
            self._name = new_name
        else:
            print("Invalid name. It must be a non-empty string.")

# Usage
person = Person("Alice")
print(person.name)  # Uses the getter to access the name

person.name = "Bob"  # Uses the setter to update the name
print(person.name)

person.name = ""  # Attempting to set an invalid name

