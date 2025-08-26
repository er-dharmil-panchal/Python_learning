# ========================================
#            POLYMORPHISM
# ========================================

"""
Polymorphism means “many forms” — the same operation or method behaves differently depending on the object or context.

In Python, it can be achieved mainly via:
    i.   Method Overriding (runtime polymorphism)
    ii.  Method Overloading (limited in Python)
    iii. Operator Overloading
"""

# ========================================
# 1️⃣ Method Overriding (Runtime Polymorphism)
# ========================================

# Parent class
class Employee:
    def greet(self):
        print("Hello from Employee")

# Child classes overriding parent method
class Manager(Employee):
    def greet(self):
        print("Hello from Manager")

class Developer(Employee):
    def greet(self):
        print("Hello from Developer")

# Polymorphism in action
print("=== Method Overriding ===")
objects = [Employee(), Manager(), Developer()]
for obj in objects:
    obj.greet()  # Calls the correct greet() based on object type
print()

# ========================================
# 2️⃣ Method Overloading (Python Style)
# ========================================

# Python does NOT support true method overloading like Java
# We can simulate it using default parameters or *args
class Calc:
    def add(self, a, b):
        return a + b

    def sum(self, a, b, c=0, d=0, e=0):  # Default parameters for flexible calls
        return a + b + c + d + e

c = Calc()
print("=== Method Overloading (Python Style) ===")
print("add(1, 2):", c.add(1, 2))
print("sum(1, 2):", c.sum(1, 2))
print("sum(1, 2, 3, 4):", c.sum(1, 2, 3, 4))
print()

# ========================================
# 3️⃣ Operator Overloading
# ========================================

class EmployeeSalary:

    def __init__(self, salary):
        self.salary = salary

    # Arithmetic Operators
    def __add__(self, other):
        return EmployeeSalary(self.salary + other.salary)

    def __sub__(self, other):
        return EmployeeSalary(self.salary - other.salary)

    def __mul__(self, other):
        return EmployeeSalary(self.salary * other.salary)

    def __truediv__(self, other):
        return EmployeeSalary(self.salary / other.salary)

    # Comparison Operators
    def __eq__(self, other):  # Equal
        return self.salary == other.salary

    def __ne__(self, other):  # Not equal
        return self.salary != other.salary

    def __gt__(self, other):  # Greater than
        return self.salary > other.salary

    def __lt__(self, other):  # Less than
        return self.salary < other.salary

    def __ge__(self, other):  # Greater or equal
        return self.salary >= other.salary

    def __le__(self, other):  # Less or equal
        return self.salary <= other.salary

    # String Representation
    # Use to display object details
    def __str__(self):
        return f"EmployeeSalary: {self.salary}"


e1 = EmployeeSalary(50000)
e2 = EmployeeSalary(60000)

print("=== Arithmetic Operators ===")
print("Add: ", e1 + e2)
print("Sub: ", e2 - e1)
print("Mul: ", e1 * e2)
print("Div: ", e2 / e1)
print()

print("=== Comparison Operators ===")
print("e1 == e2:", e1 == e2)
print("e1 != e2:", e1 != e2)
print("e1 > e2:", e1 > e2)
print("e1 < e2:", e1 < e2)
print("e1 >= e2:", e1 >= e2)
print("e1 <= e2:", e1 <= e2)
print()

print("=== String Representation ===")
print(e1)
print(e2)