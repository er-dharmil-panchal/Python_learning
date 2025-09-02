"""
📌 Functools :- built-in Python module that provides higher-order functions and tools to manipulate or enhance functions.
    - partial
    - reduce
    - lru_cache
    - wraps
"""

import time
import functools as ft

"""
Uses :-
    - Reusing code efficiently
    - Caching results
    - Simplifying repetitive tasks
    - Functional programming patterns
"""

# -----------------------------------------------------------------------------------------
# 👉🏻 Partial Function :- partial()
# -----------------------------------------------------------------------------------------
"""
    - Pre-fill some arguments of a function so you don’t repeat them.
Why to use ??
    - Avoid repetition - No need to repeatedly type the same argument in multiple calls.
    - Many libraries (Tkinter, threads, async) require a function with specific arguments. partial lets you pre-fill some arguments.
"""


def display(name, msg):
    return f"{msg}, {name}!"


say_hello = ft.partial(display, msg='Hello')
say_bye = ft.partial(display, msg='Bye')
print(say_hello("Dharmil"))
print(say_bye("Dharmil"))


# Using partial, we create a new function say_hello that already has msg="Hello","Bye" pre-filled.

def power(base, exponent):
    return base ** exponent


square = ft.partial(power, exponent=2)
cube = ft.partial(power, exponent=3)

print(square(5))  # 25
print(cube(2))  # 8

# With map
numbers = [1, 2, 3, 4, 5, 6]
print(list(map(square, numbers)))

# Summary
# partial = pre-fill some arguments of a function
# Makes code cleaner, DRYer, and easier to reuse
# Works great for callbacks, higher-order functions, and repeated arguments

# -----------------------------------------------------------------------------------------
# 👉🏻 Reduce Function :- reduce()
# -----------------------------------------------------------------------------------------
"""
reduce() - Already learned (open day-25 -> core_functional_tools.py)
"""

# -----------------------------------------------------------------------------------------
# 👉🏻 lru_cache()
# -----------------------------------------------------------------------------------------
"""
    - lru_cache stands for Least Recently Used cache. 
    - It is a decorator from the functools module.
    - Automatically stores the results of expensive or repetitive function calls so they don’t need to be recalculated.
    - Very useful for recursive functions, API requests, or heavy computations.

    Syntax :-
        @lru_cache(maxsize=128)
        def my_function(args):
            # expensive computation
            return result

maxsize → how many recent results to store; if None, unlimited caching
"""


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


f0 = 0
f1 = 1
start = time.time()
print("\nWithout Cache (1st time):")
print(fib(30))
end = time.time()
print(f"Time taken (no cache): {end - start:.6f} seconds")

start = time.time()
print("\nWithout Cache (2st time):")
print(fib(30))
end = time.time()
print(f"Time taken (no cache): {end - start:.6f} seconds")

start = time.time()
print("\nWithout Cache (3st time):")
print(fib(30))
end = time.time()
print(f"Time taken (no cache): {end - start:.6f} seconds")


@ft.lru_cache(maxsize=32)
# maxsize=32 = The cache can store results of up to 32 unique function calls (based on their arguments).
# -> If you call the function with more than 32 unique argument combinations, the least recently used (oldest) cached entry will be removed to make space for the new one.
# usually 32 considered as default , good balance between memory and performance

def fib1(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


start = time.time()
print("\nWith Cache (1st time):")
print(fib1(30))
end = time.time()
print(f"Time taken (cache): {end - start:.6f} seconds")

start = time.time()
print("\nWith Cache (2st time):")
print(fib1(30))
end = time.time()
print(f"Time taken (cache): {end - start:.6f} seconds")

start = time.time()
print("\nWith Cache (3st time):")
print(fib1(30))
end = time.time()
print(f"Time taken (cache): {end - start:.6f} seconds")

"""
    Without Cache :- 0.101916 -> 0.103418
    With cache :- 0.101916 -> 0.000002
"""

# NOTE:
# If the function arguments change each time, caching won't speed it up.
# lru_cache improves performance only when the SAME function is called
# with the SAME arguments repeatedly, as it can reuse the stored result.

# -----------------------------------------------------------------------------------------
# 👉🏻 Wraps Function :- wraps()
# -----------------------------------------------------------------------------------------
"""
    - When you create a decorator for a function, Python actually replaces the original function with your wrapper function.
    - This means the original function’s name, docstring, and metadata are lost.
    - functools.wraps fixes this by copying metadata from the original function to the wrapper.
    - It copies attributes like __name__, __doc__, __module__, __annotations__, __dict__.
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(name):
    """Say hello"""
    print(f"Hello, {name}!")


print(greet.__name__)  # wrapper  ❌ (not greet)
print(greet.__doc__)  # None     ❌ (docstring lost)


def my_decorator(func):
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(name):
    """Say hello, With Wraps"""
    print(f"Hello, {name}!")


print(greet.__name__)  # greet ✅
print(greet.__doc__)  # Say hello ✅

# -----------------------------------------------------------------------------------------
# 👉🏻 total_ordering
# -----------------------------------------------------------------------------------------
"""
    - functools.total_ordering is a class decorator that automatically fills in missing comparison methods.
    - Reduces boilerplate for classes that need full comparison support (<, <=, >, >=).
    - __eq__() must be defined along with one ordering method (__lt__, __le__, __gt__, or __ge__).
"""


@ft.total_ordering
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


s1 = Student("Dharmil", 85)
s3 = Student("Dharmil", 85)
s2 = Student("Amit", 90)

print(s1 == s3)  # True
print(s1 < s2)  # True
print(s1 <= s2)  # True (auto-generated)
print(s1 > s2)  # False (auto-generated)
print(s1 >= s2)  # False (auto-generated)

# -----------------------------------------------------------------------------------------
# 👉🏻 cmp_to_key
# -----------------------------------------------------------------------------------------
"""
📌 cmp_to_key :- it converts your old-style comparison function into a key function that Python 3 sorting can use.
    - In Python 2, you could sort using a cmp function like: sorted(data, cmp=my_cmp_function)
    - But in Python 3, the cmp argument was removed.
    - Now, sorted() and .sort() only accept a 'key function', 'not a comparator'.

Syntax :-
    sorted(iterable, key=cmp_to_key(compare_func))
"""

"""
Comparator vs Key:
->> Comparator :- compares two items and decides their order.
    Returns -1, 0, or 1.
->> Key :- extracts a value for sorting from each item.
"""


def compare(a, b):
    return (a > b) - (a < b)


nums = [5, 2, 9, 1, 7]
print(sorted(nums, key=ft.cmp_to_key(compare)))

# Using key
nums = [5, 2, 9, 1, 7]
print(sorted(nums, key=lambda x: x))

# Use key whenever possible (simpler, faster, Pythonic).
# Use comparator (cmp_to_key) only for multi-level custom logic, porting old code, or dynamic comparisons.
