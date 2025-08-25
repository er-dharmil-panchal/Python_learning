"""
📌 Class & Objects
"""


# This is user-defined object which we can create using the class keyword

class Person:
    name = "Dharmil"
    age = 18
    height = 180  # in cm

    # Instance method
    def information(self):
        print(f"Person name: {self.name}\nPerson age: {self.age}\nPerson height: {self.height}")
        # print(f"Person name {name} age: {age} height: {height}")
        # it gives error : NameError: name 'name' is not defined. Did you mean: 'self.name'?

# What is self?
# -> is a reference to the specific object (instance) that is calling the method.

# Creating object
# -> object_name = class_name()
a = Person()
a.information()

# if I want to change the name or any other properties
a.name = "Nihar"
a.age = 20
a.information()

b = Person()
b.age = 21      # just age will be change for b , name will be "Dharmil", and height will be 180 as default
b.information()

"""
There are mainly 3 types of methods in a class
i. class methods
ii. instance methods
iii. static methods

NOTE:-
--> "Every instance method in Python must have self as its first parameter, 
    which represents the specific instance (object) that is calling the method."
--> "Every class method in Python must have cls as its first parameter, 
    which represents the class itself and allows access or modification of class-level variables and methods."
--> "A static method in Python does not take self or cls as the first parameter, 
    as it neither depends on the instance nor the class and behaves like a regular function inside the class."
"""

class Method:
    a1 = 5
    b1 = 10

    # Instance method
    def instance1(self):
        return self.a1

    # Static method
    @staticmethod
    # NOTE:- in static methods, the method can't access the class instance variable directly
    #        we have to pass it in the method
    def static1(number):
        return number

    # Class method
    @classmethod
    def class1(cls):
        return cls.a1


# Instance method -> need object
obj = Method()
print(obj.instance1())

# Static method -> can be accessed by class name, but can't access the class properties directly
print(Method.static1(obj.a1))

# Class method -> can be accessed by class name and can access class properties
print(Method.class1())


"""
📌 Why Static Methods in Python?

Static methods are used when:
- The functionality is **logically related** to the class
- BUT it **does not need**:
    - Access to **class-level data** (`cls`)
    - Access to **instance-level data** (`self`)

Think of static methods like the "cleaner" in a company:
- The cleaner **belongs to the company** (logically part of it)
- But the cleaner **doesn't interact** with company policies, salaries, or management decisions
- The cleaner **just does their independent job** — like cleaning the office
"""

# Example

class GoogleCompany:
    company_name = "Google"
    employees = []

    # NOTE: This is called the *constructor* in Python.
    # It runs automatically whenever you create a new object of the class.
    # We'll learn constructors in detail later — for now, just remember:
    # -> It sets up (initializes) data for each new object (instance).
    def __init__(self, name):
        self.name = name
        GoogleCompany.employees.append(name)

    # Instance Method → Works for specific employee
    def show_details(self):
        print(f"Employee: {self.name} | Company: {self.company_name}")

    # Class Method → Works for the company itself
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

    # Static Method → Works independently (like a cleaner)
    @staticmethod
    def clean_office():
        print("🧹 Office cleaned. Everything is fresh and tidy!")

# ------------------ USAGE ------------------

# Static method usage (no need for instance or class data)
GoogleCompany.clean_office()

# Adding employees (instance method)
emp1 = GoogleCompany("Alice")
emp2 = GoogleCompany("Bob")
emp1.show_details()
emp2.show_details()

# Changing company name (class method)
GoogleCompany.change_company_name("Alphabet Inc.")

# Cleaner still works independently
GoogleCompany.clean_office()


"""
📌 Constructor
    A constructor is a special method in a class that is used to **create and initialize an object**.
    It runs automatically whenever an object of the class is created.
    
    Key Points:
    - Used to set up basic information or properties of the object at creation time.
    - Helps avoid repetitive code for assigning values manually after creating the object.
    
    NOTE: The constructor is usually defined with `__init__`.
"""

class car:
    name = "BMW"
    def __init__(self, name=None):
        if name is not None:
            self.name = name
            print(f"Quine of Germany - {self.name}")
        else:
            print(f"Not from Germany")
            # print(f"{name}")
#__init__ is reserved function in python , and it is Constructor in OOP

Mercs = car("Mercedes")
print(Mercs.name)      # Mercedes
BMW = car("BMW")

Hyundai = car()        # we have te create a constructor with no argument