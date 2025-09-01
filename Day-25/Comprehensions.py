"""
📌 Comprehensions (Already learned but quick revision)
    - A short, readable way to create new sequences (lists, sets, dicts)
      by looping through an iterable, optionally filtering with a condition.
"""

# -------------------- List Comprehensions --------------------

nums = [1, 2, 3, 4, 5]

# Get squares
squares = [x ** 2 for x in nums]
print(squares)  # [1, 4, 9, 16, 25]

# Only even squares
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # [4, 16]

# Create pairs
pairs = [(x, y) for x in [1, 2, 3] for y in [10, 20, 30, 40]]
print(pairs)
# [(1, 10), (1, 20), (1, 30), (1, 40), (2, 10), (2, 20), (2, 30), (2, 40), (3, 10), (3, 20), (3, 30), (3, 40)]

# Wrong approach with generator directly in print
print((x * y) for x in [1, 2, 3] for y in [10, 20, 30, 40])
# ❌ This will not give needed ans, we must have to do in list

# Correct approaches
print([(x * y) for x in [1, 2, 3] for y in [10, 20, 30, 40]])
# [10, 20, 30, 40, 20, 40, 60, 80, 30, 60, 90, 120]

print(list((x * y) for x in [1, 2, 3] for y in [10, 20, 30, 40]))

# Conditional expressions
labels = ["even" if x % 2 == 0 else "odd" for x in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# -------------------- Set Comprehensions --------------------
# Uses {} instead of []

nums = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x ** 2 for x in nums}
print(unique_squares)  # {1, 4, 9, 16, 25}

# -------------------- Dictionary Comprehensions --------------------
# Syntax: {key_expr: value_expr for item in iterable if condition}

nums = [1, 2, 3, 4]
dic = {1: 2, 3: 4}

# Square values from dictionary
squares = {x: y ** 2 for x, y in dic.items()}
print(squares)  # {1: 4, 3: 16}

# Squares from list
print({x: x ** 2 for x in nums})
# {1: 1, 2: 4, 3: 9, 4: 16}

# Filtered dictionary
students = {'Dharmil': 85, 'Ansh': 45, 'Nihar': 92}
print({name: marks for name, marks in students.items() if marks >= 50})
# {'Dharmil': 85, 'Nihar': 92}

# Swap keys and values
data = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in data.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# -------------------- Generator Expressions --------------------
# Use () instead of []. Creates a lazy generator object (doesn’t build a full list in memory).

nums = range(1, 10)
gen = (x ** 2 for x in nums)

print(gen)  # <generator object ...>
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # 16
print(list(gen))  # [25, 36, 49, 64, 81] (remaining values)

# -------------------- Memory Difference --------------------
# Large data example

big_list = [x for x in range(1000000)]  # occupies big memory
big_gen = (x for x in range(1000000))  # almost zero memory usage
