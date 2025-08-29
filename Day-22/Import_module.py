"""
📌 Import.
Importing in Python is the process of loading code from a Python module into the current script.
This allows you to use the functions and variables defined in the module in your current script.
"""

# also if imported module is dependent on other module that will also import here.
import math

# in math there is multiple function to use
# Convert angle x from degrees to radians.
print(math.radians(180))        # 3.14....
print(math.remainder(12, 3.5))

# Return the sine of x (measured in radians).
print(math.sin(math.radians(90)))
print(math.sinh(math.radians(90)))
print(math.cos(math.radians(0)))
print(math.cosh(math.radians(0)))
print(math.tan(math.radians(0)))  # and many more


# ----------------------------------------------------
# From keyword: import only required properties
# ----------------------------------------------------
from math import exp2, ceil

pi = 3
print(exp2(1))      # 2^1
print(exp2(10))     # 2^10
print(ceil(0.000001))

print(pi)           # 3
print(math.pi)      # if math imported then -> 3.141592653589793


# ----------------------------------------------------
# Import everything (NOT RECOMMENDED)
# ----------------------------------------------------
from math import *
print(sqrt(16))


# ----------------------------------------------------
# 'as' keyword
# ----------------------------------------------------
import math as m
from math import sqrt as s, ceil as c

print(m.sqrt(16))
print(s(16))
print(c(0.1))


# ----------------------------------------------------
# dir function (explore module attributes)
# ----------------------------------------------------
print(dir(math))


# ----------------------------------------------------
# Importing my other file (definition_practice.py)
# ----------------------------------------------------
"""
def fibo(n):
    a = 0
    b = 1
    c = 0
    print(a, end=',')
    for i in range(2, n+1):
        print(b, end=',')
        c = a
        a = b
        b = a+c
    print()
"""
from definition_practice import isPrime as f
f(10)

"""
📌 Note:
    It is giving ans True True 2 True but the actual ans should be just True.
    What is happening???
    Python loads the entire file when we import.
    When I run definition_practice the output is exact same.
    How to handle it???
"""


# ----------------------------------------------------
# __name__ == "__main__"
# ----------------------------------------------------
"""
Solution:
    lets create a sub.py which looks like this:

    print("Hello, This is before __name__")
    print(f"__name__ is {__name__}")

    def display():
        print("Hello this is from sub.py")

    if __name__ == "__main__":
        display()

Why?
    - It will check if the file is running directly.
    - If we import this, then __name__ becomes __sub__ so it is not __main__.
    - Thus, the function will not run during the importing.
"""

from sub import display, name
display()
print(__name__)     # __main__
print(name)         # sub


# ----------------------------------------------------
# Importing from package
# ----------------------------------------------------
from pkg_sub.sub import name
print(name)


# ----------------------------------------------------
# DYNAMIC IMPORTS (importlib)
# ----------------------------------------------------
import importlib

math_module = importlib.import_module('math')
print(math_module.sqrt(25))   # 5.0

# Why to use?
#   - You don’t know the module name until runtime
#   - You want to load optional modules only when needed.

module_name = input("Enter module to import (math, random): ")
module = importlib.import_module(module_name)

if module_name == "math":
    print(module.sqrt(36))
elif module_name == "random":
    print(module.randint(1, 10))


# ----------------------------------------------------
# MODULE CACHING (sys.modules)
# ----------------------------------------------------
"""
Python loads the module into memory only once.
It stores the module object in a dictionary called sys.modules.
Any subsequent 'import math' in the same program doesn’t reload the module;
it just fetches the cached version from sys.modules.
"""
import sys
import math

# Checks if 'math' exists in the cache.
print('math' in sys.modules)   # True -> math module is cached
print(sys.modules['math'])     # Shows path & module details

print('time' in sys.modules)
print(sys.modules['time'])

# Reloading a module
importlib.reload(math)         # Forces reloading of math module
# Use when you change the module and force to reload the module


# ----------------------------------------------------
# CIRCULAR IMPORTS (Concept only)
# ----------------------------------------------------
"""
Imagine:
    a.py imports b.py
    b.py imports a.py
This can cause ImportError or NoneType issues.

Solution:
    - Move common logic to a third module (e.g., common.py)
    - Import functions inside functions (local imports)
"""


# ----------------------------------------------------
# CONTROLLED IMPORTS WITH __all__
# ----------------------------------------------------
"""
Only the names in __all__ are imported with *
Example module: custom_module.py

__all__ = ['greet']             # Only these names will be imported with *

def greet():
    print("Hello from custom_module!")

def hidden():
    print("You shouldn't see me in * imports")
"""
from pkg_sub.custom_module import *
greet()       # Works
# hidden()      # NameError: hidden not imported

# Protects internal helper functions from being accidentally exposed.
# Can still import hidden function explicitly:
# from pkg_sub.custom_module import hidden