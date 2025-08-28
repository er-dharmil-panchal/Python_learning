"""
📌 Instance vs Class variable (OOP)
    - In Python, variables can be defined at the class level or at the instance level.
"""

# -----------------------------
# Class variable
# -----------------------------
# Class variables are defined at the class level and are shared among all instances of the class.
# They are defined outside of any method and are usually used to store information that is common to all instances of the class.

class student:
    school_name = "School Name"
    student_count = 0

    def __init__(self, name, age):
        self.name = name                # These both are instance variable which change according to the instance
        self.age = age
        student.student_count += 1

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


student1 = student("Nihar", 19)
student1.display()
student2 = student("Dharmil", 18)
student2.display()


# Accessing class variables
print(f"{student1.name} is in School {student1.school_name}")
print(f"{student2.name} is in School {student2.school_name}")


# Overriding class variable for a particular instance
student1.school_name = "!! Changed school name"
print(f"{student1.name} is in School {student1.school_name}")
print(f"{student2.name} is in School {student2.school_name}")


# Modifying class variable for all instances
student.school_name = "New School"
print(f"{student1.name} is in School {student1.school_name}")  # instance override still applies
print(f"{student2.name} is in School {student2.school_name}")


print(f"There are total {student.student_count} students in {student.school_name}")


# -----------------------------
# Mutable class variables (like dict, list, set)
# -----------------------------
class Test:
    data = []  # mutable class variable

t1 = Test()
t2 = Test()

t1.data.append(5)  # modifies the shared list
print(f"t1.data: {t1.data}")
print(f"t2.data: {t2.data}")  # also [5] → shared

# To avoid sharing, create instance variable
t1.data_instance = []
t1.data_instance.append(10)
print(f"t1.data_instance: {t1.data_instance}")
# t2.data_instance does not exist

# 👉🏻 NOTE:- Use class variables for shared constants, counters, or settings