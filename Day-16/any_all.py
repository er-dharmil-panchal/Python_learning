"""
===========================================================
📌 Topic: any() and all() in Python
===========================================================

any(iterable)
    - Returns True if at least one element in the iterable is True.
    - Returns False only if all elements are False or iterable is empty.

all(iterable)
    - Returns True if all elements in the iterable are True.
    - Returns False if any element is False or iterable is empty.

Common Use Cases:
    - Validations
    - Conditional checks
    - Cleaner and more readable code
===========================================================
"""

# ---------------------------------------------------------
# Example 1: any() checks if at least one condition is True
# ---------------------------------------------------------
marks = [0, 35, 0, 0]
print(any(marks))  # True (because 35 is non-zero = True)


# ---------------------------------------------------------
# Example 2: all() checks if all conditions are True
# ---------------------------------------------------------
passed = [True, True, True]
print(all(passed))  # True (all are True)


# ---------------------------------------------------------
# Example 3: Validate user inputs
# ---------------------------------------------------------
inputs = ["name", "email", "phone"]
print("Valid" if all(inputs) else "Missing info")


# ---------------------------------------------------------
# Example 4: Check if at least one positive number exists
# ---------------------------------------------------------
nums = [-1, -2, 5, -3]
print("Positive exists" if any(n > 0 for n in nums) else "All negative")


# ---------------------------------------------------------
# Example 5: Validate password strength
# ---------------------------------------------------------
password = "Hello123"
password_checks = [
    any(ch.isupper() for ch in password),  # Has uppercase
    any(ch.isdigit() for ch in password),  # Has digit
    len(password) >= 8                     # Has min length
]
print("Strong password" if all(password_checks) else "Weak password")
# If all are true then show "Strong password"