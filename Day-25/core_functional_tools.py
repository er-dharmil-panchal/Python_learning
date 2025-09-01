"""
📌 Core Functional Tools
    - Lambda
    - Map
    - Filter
    - Zip
    - Enumerate
    - Reduce
"""

# ===================================================================
# 📌 Lambda Function
# ===================================================================
"""
    - small anonymous function without a name.
    - It is defined using the lambda keyword.
    - often used in situations where a small function is required for a short period of Time
    - use in higher order function as argument like (map, filter, reduce ...)
"""


# ---------------- Syntax ----------------------
#       lambda argument : expression

# Normal function to double the value
def double(x):
    return x * 2


# lambda function to double the value
d2 = lambda x: x * 2
print(d2(5))

addition = lambda x, y: x + y
print(addition(3, 4))

# Direct call
print((lambda a, b: a + b)(3, 4))

# Celsius to Fahrenheit (F = (C * (9/5)) + 32)
c_to_f = lambda c: (c * (9 / 5)) + 32
print(c_to_f(100))
print((lambda c: (c * (9 / 5)) + 32)(100))


# Where mainly lambda use??
# For complex logic using lambda is not recommended
# When we have to pass function as an argument, then lambda is the best choice

# normal way
def cube(x):
    return x ** 3


def func(fx, value):
    return fx(value) + 12


print(func(cube, 10))  # 1012

# using lambda
print(func(lambda x: x ** 3, 10))  # 1012

# ===================================================================
# 📌 Map Function
# ===================================================================
"""
    map() - Apply a function to each element
    Syntax :- map(function, iterable) 
        - Takes a function and applies it to every element of an iterable (like a list, tuple, set, etc.).
    👉🏻 NOTE - Returns a map object (convert to list, tuple, etc.).
    - Lazy evaluation - Doesn't process until you iterate

    you can think of map() as a loop that applies a function to each element — 
    but in a more compact and expressive way.
"""

numbers = [1, 2, 3, 4, 5]

# Lambda with map
squares = map(lambda x: x * x, numbers)
print(squares)  # <map object ...>
print(list(squares))
print(list(map(lambda x: x * x, numbers)))


# With normal function
def cube(num):
    return num ** 3


numbers = [1, 2, 3]
print(list(map(cube, numbers)))

# With multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8]  # only 2 elements

print(list(map(lambda x, y: x + y, a, b)))
print(list(map(lambda x, y: x * y, a, b)))
print(list(map(lambda x, y: x * y, c, b)))
print(f"Multiplying 3 list elements :- {list(map(lambda x, y, z: x * y * z, a, b, c))}")

# Clean up strings
names = ["    Dhamril   ", " anSh   ", " jiya  "]
clean_name = list(map(lambda x: x.strip().capitalize(), names))
print(clean_name)

# ===================================================================
# 📌 Filter Function
# ===================================================================
"""
    filter() - Keep elements that satisfy a condition
    Syntax :- filter(function, iterable)
        - Takes a function and an iterable
        - Keeps only the elements where the function returns True
    👉🏻 NOTE - Returns a filter object (lazy like map)
"""

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))


# Normal function for positivity
def is_positive(num):
    return num > 0


nums = [-5, -1, 0, 2, 4, 7]
print(list(filter(is_positive, nums)))

# Multiple conditions
nums = [1, 2, 3, 6, 9, 12, 15]
print(list(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums)))
print(list(filter(lambda x: x % 2 == 0 or x % 3 == 0, nums)))

# Students example
students = ["Dharmil", "Priya", "Amit"]
marks = [90, 45, 60]
passed_students = list(filter(lambda x: marks[students.index(x)] >= 50, students))
print(passed_students)

# Remove falsy values
names = ["Dharmil", "  ", "", "Ansh", "   Jiya   "]
clean_names = filter(lambda x: x.strip(), names)
print(list(clean_names))

# ===================================================================
# 📌 Reduce Function
# ===================================================================
"""
    reduce()
    Syntax :- reduce(function, iterable, initializer)
        - Reduces a sequence of elements to a single value cumulatively.
    👉🏻 NOTE - Takes 'two elements' at a time, combines, and continues until one value remains.
"""

from functools import reduce

numbers = [10, 2, 3, 4, 5]

# Sum
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

# Product with initializer
print(reduce(lambda x, y: x * y, numbers, 2))

# Using initializer for sum
print(reduce(lambda x, y: x + y, numbers, 10))

# Max
print(reduce(lambda x, y: x if x > y else y, [12, 43, 23, 62, 12]))

# Min
print(reduce(lambda x, y: x if x < y else y, [12, 43, 23, 62, 12]))

# ===================================================================
# 📌 Mix of map, filter and reduce
# ===================================================================
a = [1, 2, 3, 4, 5, 6, 7]

# Map + Filter
print(list(filter(lambda x: x < 10, map(lambda x: x ** 2, a))))

# Map + Reduce
print(reduce(lambda x, y: x * y, map(lambda x: x * 2, a)))

# Filter + Reduce
print(reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, a)))

# Map + Filter + Reduce
print(reduce(lambda x, y: x + y, filter(lambda x: x > 5, map(lambda x: x * 2, a))))

# NOTE:
# map → transform
# filter → select
# reduce → combine

# ===================================================================
# 📌 Zip Function
# ===================================================================
"""
    zip()
    - Combine multiple iterables element-wise into tuples
"""

a = [1, 2, 3]
b = ['a', 'b', 'c']

zipped = zip(a, b)
zipped2 = zip(a, b)
print(list(zipped))
a1, b1 = zip(*zipped2)
print(list(a1))
print(list(b1))

# ===================================================================
# 📌 Enumerate Function
# ===================================================================
"""
    enumerate()
    - Add an index to each element in an iterable
"""

fruits = ['apple', 'banana', 'cherry']

for i, fruit in enumerate(fruits):
    print(i, fruit)

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

print(list(enumerate(fruits, start=1)))

# ===================================================================
# 📌 Summary Table
# ===================================================================
"""
| Function    | Purpose                                  | Returns          | Applies Function? |
| ----------- | ---------------------------------------- | ---------------- | ----------------- |
| map()       | Transform each element                   | map object       | Yes               |
| filter()    | Keep elements that satisfy condition     | filter object    | Yes               |
| reduce()    | Combine all elements into a single value | single value     | Yes               |
| zip()       | Group elements from multiple iterables   | zip object       | No                |
| enumerate() | Add index to elements                    | enumerate object | No                |
"""
