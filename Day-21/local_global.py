# -----------------------------
# Example 1: Global vs Local
# -----------------------------
x = 15  # Global variable

def num():
    x = 10         # Local variable
    name = "Python"  # Local variable
    print(x)       # Prints local x → 10

num()  
print(x)           # Prints global x → 15
# print(y)         # ERROR: y is not defined

# -----------------------------
# Accessing and Modifying Global Variables
# -----------------------------
def func():
    global y, x     # Declare x and y as global
    x = 13          # Modifies global x
    y = 10          # Creates global y
    print(y)

func()
print(f"Global x is {x}")  # 13
print(f"Global y is {y}")  # 10

# NOTE: Generally, modifying global variables inside functions is discouraged,
# as it can lead to unexpected behavior and makes debugging harder.

# -----------------------------
# Example 2: Nested Functions and Nonlocal
# -----------------------------
x = 100  # Global variable

def outer():  # 1st layer
    y = 50   # Local to outer()

    def middle():  # 2nd layer
        z = 20     # Local to middle()

        def inner():  # 3rd layer
            a = 5  # Local to inner()
            print(f"Inner local a: {a}")  # 5

            # Modify middle() variable using nonlocal
            nonlocal z
            z += 10
            print(f"Inner modified z (nonlocal from middle): {z}")  # 30

            # Modify outer() variable using nonlocal
            nonlocal y
            y += 5
            print(f"Inner modified y (nonlocal from outer): {y}")  # 55

            # Modify global variable using global
            global x
            x += 50
            print(f"Inner modified x (global): {x}")  # 150

        inner()
        print(f"Middle z after inner(): {z}")  # 30 (modified by inner)
        print(f"Middle y after inner(): {y}")  # 55 (modified by inner)

    middle()
    print(f"Outer y after middle(): {y}")  # 55 (modified by inner)
    # z is local to middle() → not accessible here

outer()
print(f"Global x after outer(): {x}")  # 150
# y and z are not accessible here → local to outer()/middle()

# -----------------------------
# 📌 IMPORTANT NOTE
# -----------------------------
# At line where middle() prints y:
# We can access outer()'s variable y without declaring it in middle().
# 👉🏻 Accessing is allowed, but modifying a variable from an outer scope requires 'nonlocal'.

"""
📌 Key Takeaways: Python Variable Scope

- local:      Refers to variables defined inside the current function; affects only this function.
- nonlocal:   Refers to variables in the nearest enclosing (outer) function; allows modification from inner functions.
- global:     Refers to variables defined at the module level; can be read or modified from any function using 'global'.
- Reading:    You can read a variable from an enclosing scope "without" using 'nonlocal'.
- Modifying:  To modify a variable from an enclosing (non-global) scope, 'nonlocal' "must be used".
"""
