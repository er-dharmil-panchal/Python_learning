"""
📌 Day 11 – Exception Handling in Python

🔹 What is Exception Handling?
- In Python, exceptions are runtime errors that may occur during program execution.
- Without handling, an exception terminates the program abruptly.
- Exception Handling allows us to catch errors gracefully and continue execution.
- Very useful when taking user input, working with files, or handling network/database operations.
"""

# ----------------------------
# 🔹 Example 1: Without Exception Handling
# ----------------------------
# a = "String" / 5       # ❌ TypeError: unsupported operand type(s) for /: 'str' and 'int'


# ----------------------------
# 🔹 Example 2: With Exception Handling
# ----------------------------
try:
    a = "String" / 5
except:
    print("Not possible")

# ✅ Output: Not possible


# ----------------------------
# 🔹 Example 3: Multiplication Table (Multiple Exceptions)
# ----------------------------
a = "Hi"        # Imagine user enters wrong input instead of a number

try:
    b = [1, 2, 3]
    print(b[88])   # ❌ IndexError
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")   # ❌ ValueError if input not a number
except ValueError as e:
    print("Value Error:", e)
except IndexError as e:
    print("Index Error:", e)

print("✅ Program continues even after exception")


# ----------------------------
# 🔹 Extra Concepts
# ----------------------------

# 1. Using else → runs only if no exception occurs
try:
    num = int("10")
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)


# 2. Using finally → always runs (cleanup, resource release)
try:
    f = open("test.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution complete (file closed, resources freed).")


"""
✅ Summary for Day-11
- try-except prevents program crashes.
- Multiple exceptions can be handled separately.
- else runs if no error, finally runs always.
- Exception handling makes programs robust and user-friendly.
"""
