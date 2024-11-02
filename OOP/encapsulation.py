class Employee:
    # Constructor
    def __init__(self, name, salary):
        self.name = name           # Public attribute
        self._department = "HR"    # Protected attribute 1(_) (should ideally be used within the class or subclass)
        self.__salary = salary     # Private attribute 2(__) (should not be accessed directly) 
    
    # Public method to display employee details
    def display_employee_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")

    # Protected method (should ideally be used within the class or subclass)
    def _access_department(self):
        print(f"{self.name} works in {self._department} department.")

    # Private method to calculate bonus, accessible only within this class
    def __calculate_bonus(self):
        return self.__salary * 0.10

    # Public method to access private bonus calculation
    def get_bonus(self):
        return self.__calculate_bonus()


# Subclass demonstrating protected access
class Manager(Employee):
    def show_department(self):
        print(f"{self.name} is in the protected department: {self._department}")


# Testing the Employee class
emp = Employee("Alice", 50000)

# Accessing public attributes and methods
print(emp.name)  # Public attribute
emp.display_employee_details()  # Public method

# Accessing protected attributes and methods (by convention, not strict)
print(emp._department)  # Protected attribute
emp._access_department()  # Protected method

# Accessing private attributes and methods
# print(emp.__salary)  # This would raise an AttributeError
# To access private members, name mangling is required:
print(emp._Employee__salary)  # Access private attribute (not recommended)

# Accessing private method indirectly
print("Bonus:", emp.get_bonus())

# Using subclass to access protected attributes
manager = Manager("Bob", 70000)
manager.show_department()
