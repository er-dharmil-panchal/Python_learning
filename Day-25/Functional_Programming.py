"""
📌 Functional Programming
"""

# ------------------ What is Functional Programming ------------------
"""
Functional Programming (FP) is a programming paradigm where programs are built using pure functions, 
immutable data, and function composition rather than relying heavily on changing states or objects.

Instead of writing code that changes data step by step (like in procedural or object-oriented programming), 
functional programming focuses on describing what to do rather than how to do it — by using functions as the main building blocks.

- Immutability :- Data is never modified; instead, you create and return new data when needed.
- First-class & Higher-order Functions :- Functions can be stored in variables, passed as arguments, and returned from other functions.
"""

# ------------------ When to use FP ------------------
"""
- Data transformations (filtering, mapping, reducing)
- Parallel/concurrent tasks - Pure functions are thread-safe (no shared state)
- Mathematical/algorithmic computations
- Reusable utilities - Pure, stateless functions can be reused anywhere
"""

# ------------------ When NOT to overuse FP in Python ------------------
"""
- When heavy mutation or state management is natural (like GUIs or game loops).
- When readability would suffer (too many nested lambdas or combinators).
"""


# ------------------ Assigning Function to a Variable ------------------
def display(name):
    return f"Hello,{name}"


say_hello = display
print("Assigning function to a variable:")
print(say_hello("Amit"))
print("-" * 50)


# ------------------ Passing Function as an Argument ------------------
def apply_function(func, value):
    return func(value)


def square(x):
    return x * x


print("Passing function as an argument:")
print(apply_function(square, 5))  # Passing function as argument
print("-" * 50)


# ------------------ Returning Functions from Functions ------------------
def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print("Returning functions from functions:")
print(double(5))  # 10
print(triple(5))  # 15
print(multiplier(8)(5))  # 100
# Note: can use direct - if 3 nested then 3 brackets, or save for 2 and use in 3rd like we do in double and triple
print("-" * 50)


# ------------------ Example: Adding Prefix ------------------
def add_prefix(prefix):
    def inner(text):
        return f"{prefix}{text}"

    return inner


add_mr = add_prefix("Mr. ")
add_ms = add_prefix("Ms. ")

print("Adding prefix example:")
print(add_mr("Dharmil"))  # Mr. Dharmil
print(add_ms("Priya"))  # Ms. Priya
print(add_prefix("Mr. ")("Dharmil"))  # can use direct
print("-" * 50)

"""
This is useful when we need multiple variations of the same function
for different purposes. Instead of rewriting the logic,
we create specialized versions and reuse them wherever needed.
"""
