# ==========================================================================================================
#                                              PYTHON OPERATORS
# ==========================================================================================================

# ---> Arithmetic Operators
# Used for basic math calculations

print("Arithmetic Operators:")
print("5 + 3 =", 5 + 3)        # Addition
print("5 - 3 =", 5 - 3)        # Subtraction
print("5 * 3 =", 5 * 3)        # Multiplication
print("5 / 3 =", 5 / 3)        # Division (float)
print("5 // 3 =", 5 // 3)      # Floor Division (int)
print("5 % 3 =", 5 % 3)        # Modulus (remainder)
print("5 ** 3 =", 5 ** 3)      # Exponentiation

print()

# ---> Assignment Operators
# Used to assign and update variable values

x = 5
print("Assignment Operators:")
print("x =", x)
x += 3      # equivalent to x = x + 3
print("x += 3 ->", x)
x *= 2      # equivalent to x = x * 2
print("x *= 2 ->", x)

print()

# ---> Comparison Operators
# Compare two values and return boolean True/False

print("Comparison Operators:")
print("5 == 5 ->", 5 == 5)     # Equal
print("5 != 3 ->", 5 != 3)     # Not equal
print("5 > 3 ->", 5 > 3)       # Greater than
print("3 < 5 ->", 3 < 5)       # Less than
print("5 >= 5 ->", 5 >= 5)     # Greater than or equal
print("3 <= 2 ->", 3 <= 2)     # Less than or equal

print()

# ---> Logical Operators
# Combine boolean values

print("Logical Operators:")
print("True and False ->", True and False)
print("True or False ->", True or False)
print("not True ->", not True)

print()

# ---> Bitwise Operators
# Operate on bits of integers

print("Bitwise Operators:")
print("5 & 3 ->", 5 & 3)       # AND
print("5 | 3 ->", 5 | 3)       # OR
print("5 ^ 3 ->", 5 ^ 3)       # XOR
print("~5 ->", ~5)             # NOT
print("5 << 1 ->", 5 << 1)     # Left shift
print("5 >> 1 ->", 5 >> 1)     # Right shift

print()

# ---> Membership Operators
# Check if a value is in a collection

print("Membership Operators:")
print("'a' in 'cat' ->", 'a' in 'cat')
print("'x' not in 'cat' ->", 'x' not in 'cat')

print()

# ---> Identity Operators
# Check if two variables refer to the same object

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity Operators:")
print("a is b ->", a is b)         # True, same object
print("a is c ->", a is c)         # False, different objects
print("a is not c ->", a is not c) # True
