"""
📌 Custom Error
In Python, we can raise a custom error by using the 'raise' keyword.
It is most useful when we need to throw an error for our particular logic in a project.
"""

# -----------------------------------------------------
# Example 1: Using an inbuilt error for a custom condition
# -----------------------------------------------------
age = int(input("Enter your age : "))
if age < 18:
    raise ValueError("You are not eligible for Driving license")


# -----------------------------------------------------
# Example 2: Defining and handling a custom error
# NOTE: Classes and OOP are not fully learned yet,
# so focus only on the concept, not the advanced part.
# -----------------------------------------------------
class ageException(Exception):
    pass  # some exception particular code...

try:
    age = int(input("Enter your age : "))
    if age < 18:
        raise ageException("You are not eligible for Driving license")
except ageException as e:
    print(e)

# Example Input:
# Input = 5
# Output = You are not eligible for Driving license


# -----------------------------------------------------
# Example 3: Basic hierarchy of exceptions (for bigger projects)
# -----------------------------------------------------
class ProjectError(Exception):  # Base error (Parent)
    pass

class InvalidAgeError(ProjectError):  # Child error
    pass

try:
    age = int(input("Enter your age : "))
    if age < 18:
        raise InvalidAgeError("Age is below 18, not eligible!")
except InvalidAgeError as e:
    print(e)
except ProjectError as e:
    print("Some other project error:", e)

# Example Input:
# Input = 15
# Output = Age is below 18, not eligible!



# QUIZ :- if user enter quit then no error should be shown
class BelowZero(Exception):
    pass

incom = input("Enter your income (must be >0): ")

if incom.lower() != "quit":
    try:
        incom = int(incom)
        if incom < 0:
            raise BelowZero("Value below 0 is not valid")
        else:
            print(f"Your income is {incom}")
    except ValueError:
        print("Please enter a valid number or type 'quit' to exit.")
