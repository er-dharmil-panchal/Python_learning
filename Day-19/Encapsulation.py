# ========================================
#         Encapsulation
# ========================================

"""
What is Encapsulation ??
    - Encapsulation is hiding the internal data of a class and controlling access to it.
    - It ensures that data is not directly accessible or modifiable from outside the class, which protects the integrity of the object.
In Python, we achieve encapsulation using:
    - Private variables (__var)
    - Protected variables (_var)
    - Getter and Setter methods to access or modify the data safely
"""

# ========================================
#         Access Modifier
# ========================================

"""
| Modifier           | Class | Subclass                 | Other classes / modules               | Notes                                     |
| ------------------ | ----- | ---------------------    | ------------------------------------  | ----------------------------------------- |
| Public (`var`)     | ✅ Yes | ✅ Yes                 | ✅ Yes                                | Default access in Python is public        |
| Protected (`_var`) | ✅ Yes | ✅ Yes (by convention) | ⚠️ Yes (by convention, not enforced)  | Convention only                           |
| Private (`__var`)  | ✅ Yes | ❌ No                  | ❌ No                                 | Name-mangled to prevent accidental access |
        (by default all properties are public)
        
IMPORTANT: 

Public properties can access by other files also(Public can access from anywhere.
Protected can also access by other files but is strongly not recommended(Details reason will explain below)
Private only ment inside a class

"""

class Employee:
    # Public variable
    company = "Google"

    # Protected variable
    _department = "Marketing"

    # Private variable
    __salary = 50000

    def __init__(self, name):
        self.name = name          # public
        self._role = "Employee"   # protected
        self.__id = 101           # private

    # Getter for private variable
    def get_salary(self):
        return self.__salary

    # Setter for private variable
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

# Other class ( also child )
class Manager(Employee):
    def show_info(self):
        print("Inside Subclass:")
        print(f"Name (public): {self.name}")        # ✅ Public
        print(f"Role (protected): {self._role}")   # ✅ Protected
        # print(self.__id)                          # ❌ Private, cannot access
        print(f"Salary (private via getter): {self.get_salary()}")  # ✅ Access via getter
        print(f"Company (public class var): {self.company}")        # ✅ Public
        print(f"Department (protected class var): {self._department}")  # ✅ Protected

# Another Class (Same File)
class HR:
    def show_employee(self, emp):
        print("Access from Another Class (Same File):")
        print(emp.name)         # ✅ Public
        print(emp._role)        # ⚠️ Protected (you can do it, but it’s not recommended.)
        # print(emp.__id)       # ❌ Private, cannot access
        print(emp.get_salary()) # ✅ Access private via getter

# Testing Access Outside Class
e = Employee("Dharmil")
print("Accessing inside main (Outside Class):")
print(e.name)          # ✅ Public
print(e._role)         # ⚠️ Protected (discouraged)
# print(e.__id)        # ❌ Private
print(e.get_salary())  # ✅ Private via getter
print()

# Testing Subclass Access
m = Manager("Kunal")
m.show_info()
print()

# Testing Another Class Access
hr = HR()
hr.show_employee(e)
print()

# Accessing Class Variables
print("Accessing class variables:")
print(Employee.company)       # ✅ Public
print(Employee._department)   # ⚠️ Protected
# print(Employee.__salary)    # ❌ Private
print()

# -------------------------------
# Notes:
# -------------------------------
# Public       -> Accessible anywhere
# Protected    -> Accessible in class/subclass (discouraged outside)
# Private      -> Accessible only via getter/setter