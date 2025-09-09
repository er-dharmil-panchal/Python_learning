"""
📌 Introduction of NumPy  (Step 1)

This file covers the fundamentals of NumPy:
- What is NumPy and why it is used
- Installation and importing
- Creating arrays from lists, tuples, strings, mixed types, dicts, sets, and booleans
- Key rules about NumPy array dtypes
- Array attributes (dtype, ndim, shape, size)
- Practice with 1D and 2D arrays
- Creating higher-dimensional arrays using ndmin

📝 Summary:
NumPy arrays are optimized for numerical computations and stored in contiguous memory.
They are typed, and NumPy promotes mixed types to a common dtype.
Non-sequence objects (like dicts or sets) are treated as a single object.
"""
# =============== Introduction =================
"""
What is NumPy?
    - NumPy (Numerical Python) is a Python library used for fast numerical computations.
    - NumPy is used for working with arrays.
    - It’s way faster than normal Python lists for math & matrix operations (50x faster than traditional Python lists).
    - Widely used in Data Science, Machine Learning, AI, Image Processing, and Scientific Computing.

Why is NumPy Fast?
    - NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
"""

# =============== Installation (If not) =================
# In terminal run this command: pip install numpy

# Standard convention to import NumPy
import numpy as np

print(np.__version__)  # 2.3.2

# =============== First Example =================

# 1. List → NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
print(f"List to array: {arr1}, dtype: {arr1.dtype}")

# 2. Tuple → NumPy array
arr2 = np.array((1, 2, 3))
print(f"Tuple to array: {arr2}, dtype: {arr2.dtype}")

# 3. String elements
arr3 = np.array(["apple", "banana", "cherry"])
print(f"Strings to array: {arr3}, dtype: {arr3.dtype}")

# 4. Mixed types (int + float → promoted to float)
arr4 = np.array([1, 2.5, 3])
print(f"Mixed int+float: {arr4}, dtype: {arr4.dtype}")

# 5. Mixed types (int + string → all become strings)
arr5 = np.array([1, "hello", 3])
print(f"Mixed int+string: {arr5}, dtype: {arr5.dtype}")

# 6. Dictionary → treated as single object
arr6 = np.array({"dharmil": 1, "raj": 2})
print(f"Dictionary to array: {arr6}, dtype: {arr6.dtype}")

# 7. Set → treated as single object
arr7 = np.array({10, 20, 30})
print(f"Set to array: {arr7}, dtype: {arr7.dtype}")

# 8. Boolean values
arr8 = np.array([True, False, True])
print(f"Booleans to array: {arr8}, dtype: {arr8.dtype}")

print(f"{type(arr8)}: {arr8.dtype}")

"""
📝 Key Rules:
- NumPy tries to make one common dtype inside an array:
    [1, 2.5] → float64
    [1, "hi"] → string
- Non-sequence objects (like dict, set) become a single object inside the array.
- That’s why np.array({"dharmil":1}) just stores the dictionary, not its elements.
"""

# Some attributes of the array
arr1 = np.array([[1, 2, 3], [33, 112, 2]])
print(arr1.dtype)   # int64
print(arr1.ndim)    # 2 → dimensions
print(arr1.shape)   # (2, 3) → 2 rows, 3 columns
print(arr1.size)    # 6 → total elements

# Practice: create a 1D array of numbers 10, 20, 30, 40
# Print: The array, its shape, ndim, dtype, size
# Create a 2D array (matrix) with numbers 1–9 and print the same attributes.

oneD = np.array([10, 20, 30, 40])
print(
    f"The 1D array is {oneD}, its shape is {oneD.shape}, size is {oneD.size}, dtype: {oneD.dtype}, dimensions: {oneD.ndim}"
)
# 1D array doesn’t really have rows or columns → just elements.
# NumPy shows (4,) → 4 elements along 1 axis

oneD = oneD.reshape(4, 1)
print(f"\nAfter reshape to (4,1)\n{oneD}")
print(oneD.shape)

twoD = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(
    f"\nThe 2D array is \n{twoD}, its shape is {twoD.shape}, size is {twoD.size}, dtype: {twoD.dtype}, dimensions: {twoD.ndim}"
)

# Can also do like this for higher-dimensional arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)         # [[[[[1 2 3 4]]]]]
print(arr.ndim)    # 5
