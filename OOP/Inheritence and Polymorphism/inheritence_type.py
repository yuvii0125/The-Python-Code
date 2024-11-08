'''
1. Single Inheritance: A child class inherits from only one parent class.

2. Multiple Inheritance: A child class inherits from multiple parent classes.

3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from 
another parent class (and so on).
 
4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

5. Hybrid Inheritance:A combination of multiple inheritance types.
'''

#2.Multiple Inheritence
class Parent1:
    def __init__(self):
        print("Parent1")

class Parent2:
    def __init__(self):
        print("Parent2")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

# Create an object of the Child class
child_obj = Child()

#3. Multilevel Inheritance
class Grandparent:
    def __init__(self):
        print("Grandparent")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")

# Create an object of the Child class
child_obj = Child()

#4. Hierarchical Inheritance
class Parent:
    def __init__(self):
        print("Parent")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Child1")

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("Child2")


#5. Hybrid Inheritance
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C:
    def __init__(self):
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")