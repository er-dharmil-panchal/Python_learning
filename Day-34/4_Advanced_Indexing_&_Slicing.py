"""
📌 NumPy – Step 4 (Advanced Indexing & Slicing)

This file covers:
    - Boolean Indexing (filtering arrays with conditions)
    - Combining multiple conditions using &, |, ~
    - Fancy Indexing (selecting using index arrays)
    - np.where() for conditional selection & replacement

📝 Summary:
    - Advanced indexing allows more powerful ways to access data in NumPy arrays.
    - Boolean indexing is used to filter values based on conditions.
    - Fancy indexing lets you select elements by custom index arrays.
    - np.where() provides vectorized conditional operations.
"""

# =============== Boolean Indexing =================
# Filtering with Conditions
# pass a True/False mask to select elements.
# Useful for filtering arrays like SQL queries.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# 1) Single condition
print(arr[arr > 25])
# [30 40 50]

# 2) Combining multiple conditions with "&" (AND)
print(arr[(arr > 15) & (arr < 45)])
# [20 30 40]

# 3) Combining multiple conditions with "|" (OR)
print(arr[(arr < 15) | (arr > 45)])
# [10 50]

# 4) Using "~" (NOT → inverts boolean mask)
mask = arr > 25
print(mask)  # [False False  True  True  True]
print(~mask)  # [ True  True False False False]
print(arr[~mask])  # [10 20] → values that are NOT > 25

# Example: Select elements that are NOT equal to 30
print(arr[arr != 30])  # [10 20 40 50]

# Example: Negating combined condition
print(arr[~((arr > 15) & (arr < 45))])
# [10 50]

# Important: Python’s built-in and / or / not do not work with NumPy arrays. That’s why we must use & | ~.

# =============== Fancy Indexing =================
# Selecting with Index Arrays
# Instead of slicing ranges, you can give specific index positions.


# Example 1 (1D):
arr = np.array([10, 20, 30, 40])
print(arr[[0, 1, 3]])  # [10 20 40]
print(arr[[0, 2]])  # [10 30]

# Example 2 (2D):

matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Select specific elements: (0,2), (1,0), (2,1)
rows = [0, 1, 2]
cols = [2, 0, 1]
print(rows)
print(cols)
print(matrix[rows, cols])  # [30 40 80]

# =============== np.where() =================
# Conditional Selection
# Like a vectorized if-else.
# Syntax: np.where(condition, value_if_true, value_if_false)

arr = np.array([10, 15, 20, 25, 30])

print(np.where(arr > 20, "Yes", "No"))  # ['No' 'No' 'No' 'Yes' 'Yes']
print(np.where(arr > 20))  # (array([3, 4]),)

# =============== Practice Task =================

# Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
filter = arr > 42
print(arr[filter])

# Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter = arr % 2 == 0
print(arr[filter])

"""
📌 Quick Recap
    - Boolean Indexing → filter values using conditions
    - Fancy Indexing → select elements by custom indices
    - np.where() → conditional element selection or replacement
"""
