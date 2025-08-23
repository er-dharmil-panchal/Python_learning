"""
📌 Short-Hand If-Else (One-Line If-Else in Python)

🔹 Syntax:
    statement_if_true if condition else statement_if_false
"""

# ------------------- Examples -------------------

# Example 1: Single condition
x = 10
print("Positive") if x > 0 else print("Negative or Zero")


# Example 2: Compare two numbers
a, b = 5, 10
print("a is bigger") if a > b else print("b is bigger")


# Example 3: Even or odd
num = 7
print("Even") if num % 2 == 0 else print("Odd")


# ------------------- Multiple Short-Hand (Nested) -------------------
"""
Syntax for multiple:
    result1 if condition1 else result2 if condition2 else result3
"""

# Example 4: Grade system based on marks
marks = 85
print("A Grade") if marks >= 90 else print("B Grade") if marks >= 75 else print("C Grade")


# Example 5: Number sign check
n = -5
print("Positive") if n > 0 else print("Zero") if n == 0 else print("Negative")
