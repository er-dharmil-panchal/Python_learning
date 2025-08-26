# ========================================
#           INHERITANCE EXAMPLES
#      (Methods, Overriding, Super Keyword)
# ========================================

# A class can inherit another class by putting the parent class name in parentheses,
# gaining its methods and properties.
class Parent:
    def car(self):
        print("Parent's car")

# Child inherits Parent without changes
class Child(Parent):
    pass


# Child2 overrides car() and adds car2() using super()
class Child2(Parent):
    def car(self):
        print("Child's car")

    def car2(self):
        super().car()  # Calls Parent's car()


c1 = Child()  # Child can access parent's car
c1.car()

c2 = Child2()  # If child has its own property same as parent, it overrides
c2.car()
c2.car2()


# ----------------------------------------
# Note: super keyword
# It is used to access properties and methods from parent class
# ----------------------------------------


# ========================================
#      INHERITANCE WITH CONSTRUCTORS
# ========================================

class Employee:
    company = "Google"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def information(self):
        print(f"Employee {self.name} has age {self.age}")


# Child Class with Constructor
class Department(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)  # Use parent constructor to assign data
        self.department = department

    def information(self):
        print(f"Department {self.name} has department {self.department}")
        # Accessing parent class property and method using super()
        print(super().company)
        print(super().information())


d = Department("Dharmil", 18, "Marketing")
d.information()


# ========================================
#      Multilevel Inheritance
# ========================================

class Parent:
    def information(self):
        print("Parent's information")

class Child(Parent):
    def information(self):
        super().information()
        print("Child information")

class GrandChild(Child):
    def information(self):
        super().information()
        print("Grandchild information")


g = GrandChild()
g.information()


# ========================================
#      Multiple Inheritance
# ========================================

class Father:
    def information(self):
        print("Father's information")

class Mother:
    def information(self):
        print("Mother's information")

class Child(Mother, Father):
    def information(self):
        super().information()


"""
Note: Python supports multiple inheritance. 
      If both parent classes have a property/method with the same name (ambiguous situation), 
      Python gives priority to the class that appears first in the inheritance list.
"""

c = Child()
c.information()     # Output: Mother's information

#IMP :- METHOD RESOLUTION ORDER (MRO)
print(Child.mro())
# O/P :- [<class '__main__.Child'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>]


# ========================================
#      Private and Protected Members
# ========================================

# Private :- Child classes cannot access directly; you’d need a getter method.
# Protected :- Child classes can access it, but it’s a warning not to access from outside.
# NOTE:- Syntax and access modifiers will be learned soon.
class Parent:
    def __init__(self):
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

    def show_private(self):
        print(self.__private_var)

class Child(Parent):
    def access_vars(self):
        print(self._protected_var)  # ✅ Accessible
        # print(self.__private_var)  # ❌ Error: cannot access directly
            # AttributeError: 'Child' object has no attribute '_Child__private_var'. Did you mean: '_Parent__private_var'?
        self.show_private()          # ✅ Access via parent method


c = Child()
c.access_vars()


# ========================================
#      Polymorphism via Inheritance
# ========================================

# Same method name, different behaviors depending on the object (child class)
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def greet(self):
        print("Hello from Child1")

class Child2(Parent):
    def greet(self):
        print("Hello from Child2")


# Polymorphism usage
objects = [Parent(), Child1(), Child2()]

for obj in objects:
    obj.greet()
