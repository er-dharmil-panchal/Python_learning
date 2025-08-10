#========================================================================================================
#========================================================================================================
#----------------------------------------- If-Else Statements -------------------------------------------
#========================================================================================================
#========================================================================================================

'''
If-else statements are used for making decisions in Python.
'''

# 👉🏻 Conditional Operators 👈🏻 : --> >, <, >=, <=, ==, != ;

a = int(input("Enter Your Age:  "))
print("Your Age is:", a)

print(a > 18)
print(a < 18)
print(a == 18)
print(a != 18)
print(a >= 18)
print(a <= 18)

if a > 18:
    print("You Can Drive\n")                
    # NOTE: You can write condition in if without using brackets (); Example: if a > 18
    # NOTE: You "cannot" write any statement inside if without indenting it (space).
    # NOTE: This space is called "Indentation".
    print("yes")
else:
    print("You Cannot Drive\n")

print("THIS LINE IS OUT FROM IF-ELSE")

# In other languages (JAVA/C) we use {} in if-else, but in Python we use indentation.

# Example:

PhonePrice = 150000
Budget = 100000

if PhonePrice >= Budget:
    print("Dharmil cannot buy Phone\n")
else:
    print("Dharmil can buy Phone\n")

# ----> elif statements

num = int(input("Enter the value of num: "))

if num > 0:
    print("Number is Positive.")
elif num < 0:
    print("Number is Negative.\n")
elif num == 13:
    print("This is a Special Number\n")
else:
    print("Number is zero.")

# In this code, 13 is a special number, but if input is '13', output shows "Number is Positive."
# So, num == 13 must be checked before num > 0.

if num == 13:
    print("This is a Special Number\n")
elif num > 0:
    print("Number is Positive.")
elif num < 0:
    print("Number is Negative.\n")
else:
    print("Number is zero.")

# THAT MEANS: If first condition is True, Python will not check any other condition.

# -----> 👉🏻 NESTED IF STATEMENTS 👈🏻

# Multiple if statements inside an if statement.

if num == 0:
    print("Number is zero\n")
elif num > 0:
    if num == 13:
        print("This is Special Number and This Number Is Positive\n")
    elif num <= 10:
        print("The number is Between 1 to 10\n")
    else:
        print("Number is Positive (either from 11 to 12 or > 13).")
elif num < 0:
    print("Number is Negative.\n")
else:
    print("Number is zero.")

#========================================================================================================
# Boolean Logic in Python: and, or, not
#========================================================================================================

# 1. and operator
# Both conditions must be True for the whole expression to be True.
# NOTE: If first condition is False, Python does NOT evaluate the second condition.

x = 5
if x > 0 and x < 10:
    print("x is between 1 and 9")  # Both conditions True, so this runs
else:
    print("x is not between 1 and 9")

# 2. or operator
# At least one condition must be True for the whole expression to be True.
# NOTE: If first condition is True, Python does NOT evaluate the second condition.

x = -3
if x < 0 or x > 10:
    print("x is either negative or greater than 10")  # x < 0 is True, so this runs
else:
    print("x is between 0 and 10 (inclusive)")

# 3. not operator
# Reverses the Boolean value of the condition.

x = 5
if not x > 10:  
    # x > 10 is False, so not False → True, this block runs
    print("x is NOT greater than 10")
else:
    print("x is greater than 10")

# Combined example using and

age = 20
has_license = True

# Both conditions must be True for you to drive
if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

#========================================================================================================
# The 'in' operator checks if a value exists inside a container (like a string, list, tuple, dictionary keys, etc.)
#========================================================================================================

# Example 1: Check if a character is in a string
if "a" in "banana":
    print("'a' is present in 'banana'")  # This will print
else:
    print("'a' is NOT present in 'banana'")

# Example 2: Check if an item is in a list
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")  # This will print
else:
    print("Banana is NOT in the list")

# Example 3: Check if a key is in a dictionary
person = {"name": "Alice", "age": 25}
if "name" in person:
    print("Key 'name' exists in the dictionary")  # This will print
else:
    print("Key 'name' does NOT exist in the dictionary")

# Example 4: Using 'not in' to check absence
if "orange" not in fruits:
    print("Orange is NOT in the list")  # This will print
else:
    print("Orange is in the list")

#========================================================================================================
# Ternary conditional expressions (inline if-else)
#========================================================================================================

# Syntax: <value_if_true> if <condition> else <value_if_false>

age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

#========================================================================================================
# Truthy and Falsy values in Python
#========================================================================================================

values = [0, "", None, [], {}, 42, "hello", [1, 2]]

for v in values:
    if v:
        print(f"{repr(v)} is Truthy")
    else:
        print(f"{repr(v)} is Falsy")

# Output:
# 0 is Falsy
# '' is Falsy
# None is Falsy
# [] is Falsy
# {} is Falsy
# 42 is Truthy
# 'hello' is Truthy
# [1, 2] is Truthy
