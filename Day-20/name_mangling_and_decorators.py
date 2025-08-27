"""
📌 NAME MANGLING IN PYTHON
Name mangling is a technique used to protect private attributes from being
accidentally overwritten by subclasses.

Python transforms:
    - Class-private attributes → _ClassName__variable
    - Superclass-private attributes → _SuperClassName__variable
"""

# ----------------------------------------------------
# 1️⃣ Basic Example of Name Mangling
# ----------------------------------------------------
class Var:
    __name = "Dharmil"   # private variable

v = Var()
# print(v.__name)   # ❌ AttributeError: 'Var' object has no attribute '__name'

# ✅ Access via name mangling
print(v._Var__name)   # Output: Dharmil


# ----------------------------------------------------
# 2️⃣ Why Name Mangling Exists (Inheritance Safety)
# ----------------------------------------------------
"""
Imagine:
- Developer A creates a class with a private variable `__balance`
- Developer B extends that class and unknowingly creates another variable with the same name
"""

class Bank:
    def __init__(self):
        self.__balance = 1000   # private in parent

    def show_balance(self):
        print(f"Parent Balance: {self.__balance}")


class MyBank(Bank):
    def __init__(self):
        super().__init__()
        self.__balance = 0   # private in child (separate variable)

    def show_child_balance(self):
        print(f"Child Balance: {self.__balance}")


obj = MyBank()
obj.show_balance()        # Access parent's private -> 1000
obj.show_child_balance()  # Access child's private -> 0

# Inspect mangled names
print(obj.__dir__())  # shows _Bank__balance and _MyBank__balance both are different


# ----------------------------------------------------
# 3️⃣ What If It Is Not Private? (No Name Mangling)
# ----------------------------------------------------
class Bank:
    def __init__(self):
        self.balance = 1000   # public variable

class MyBank(Bank):
    def __init__(self):
        super().__init__()
        self.balance = 0   # accidental overwrite

# Test
obj = MyBank()
print(obj.balance)   # Output: 0 (parent's value lost)


# NOTE:-
# So as we see, if there is no name mangling, there is a chance to lose or overwrite data.
# But due to name mangling, Python keeps each class's private variable separate and safe.


"""
📌 Decorators
    A decorator is simply a function that wraps another function to add extra functionality without modifying the original code.
    - A function that takes another function as input
    
    In Python, functions are first-class objects:
        - You can pass them as arguments
        - You can return them from other functions
        - You can store them in variables
"""

def greet():
    print("Hello!")

say_hello = greet  # assigning function to a variable
say_hello()        # Output: Hello!


# How a decorator works, first build it manually
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()  # calling the original function
        print("After function execution")
    return wrapper

def greet():
    print("Hello World!")

# 👉🏻 Manually decorating: we pass the main function in the decorator manually as an argument
decorated_function = my_decorator(greet)
decorated_function()

# Instead of doing this manually, we can use @decorators
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()  # calling the original function
        print("After function execution")
    return wrapper

@my_decorator               # <-----
def greet():
    print("Hello World!")

greet()
# The @my_decorator tells Python to pass `greet` into `my_decorator` and replace it with the returned wrapper.


# Let's take an example with parameters
# kwargs stands for "keyword arguments." It allows a function to accept any number of named arguments without knowing their names in advance.
def my_decorator(func):
    def wrapper(*args, **kwargs):       # IMP
        print("Before execution")
        func(*args, **kwargs)
        print("After execution")
    return wrapper

@my_decorator
def add(a, b):
    print(f"Sum: {a + b}")

add(5, 10)


# kwargs --->
def greet(**kwargs):
    print(kwargs)

greet(name="Dharmil", age=18, country="India")


def show_details(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_details(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name="Dharmil", city="Ahmedabad")


# Examples
# 1
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with args {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def multiply(x, y):
    return x * y

print(multiply(3, 4))


# 2
def requires_login(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            print("Access Denied!")
            return
        return func(user)
    return wrapper

@requires_login
def dashboard(user):
    print(f"Welcome, {user['name']}!")

dashboard({"name": "Dharmil", "is_logged_in": True})    # Welcome Dharmil!
dashboard({"name": "Dharmil", "is_logged_in": False})   # Access Denied!


# Inbuilt decorators

# i. @property & @func.setter

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

c = Circle(5)
# c.radius = 10                 # AttributeError: property 'radius' of 'Circle' object has no setter
print(c.radius)  # 5


# Setter
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

c = Circle(5)
c.radius = 15       # setter called
print(c.radius)     # getter called


# 2. @staticmethod (Already learned)
# Used to define a method that belongs to the class, not to the object.
# Does not take self or cls as the first argument.
# Can be called using class name or object.


# 3. @classmethod (Already learned)
# Defines a method that belongs to the class itself, not instances.
# Takes cls as the first argument.
# Often used as factory methods.


# NOTE :- There are many more, but they will be learned by using them with time.
