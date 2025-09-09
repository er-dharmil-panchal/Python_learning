"""
📌 NumPy Basics – Step 2 (Array Creation, Indexing, Slicing, Reshape, Flatten & Transpose)

This file covers:
- Different ways to create NumPy arrays (zeros, ones, empty, arange, linspace, identity, full)
- Indexing & slicing in 1D and 2D arrays
- Reshaping arrays (1D ↔ 2D)
- Practice examples
- Flattening & transposing arrays

📝 Summary:
NumPy provides flexible methods to create arrays and manipulate them.
Indexing, slicing, and reshaping are fundamental for working with arrays efficiently.
Flatten and transpose help in array dimensional transformations.
"""

import numpy as np

# =============== Array Creation =================

"""
    NumPy provides many ways to create arrays besides np.array. 
"""
arr = np.zeros([1, 3, 5, 4])
# Axis 0 = 1 → “block”
# Axis 1 = 3 → “row”
# Axis 2 = 5 → “sub-row”
# Axis 3 = 4 → “column”

# Numpy support 32 dimensions
print(arr)

# 👉🏻 1. np.zeros – Create an array filled with 0
arr = np.zeros((1, 2))
print(arr)
print(arr.shape, arr.dtype)

# 👉🏻 2. np.ones – Create an array filled with 1
arr = np.ones((1, 2))
print(arr)
print(arr.shape, arr.dtype)

# 👉🏻 3. np.empty – Create an uninitialized array
# NOTE :- Note: Values are random garbage memory values, not zeros.
empty_arr = np.empty((1, 2))
print(empty_arr)
print(empty_arr.shape, empty_arr.dtype)

# 👉🏻 4. np.arange – Create sequence (like Python range)
range_arr = np.arange(0, 1000, 50)  # start, stop, step
print(range_arr)

# 👉🏻 5. np.linspace – Create n evenly spaced numbers
linspace_arr = np.linspace(1, 2, 5)
print(linspace_arr)  # [1.   1.25 1.5  1.75 2.  ]

# 👉🏻 6. np.eye / np.identity – Identity matrix
identity_arr = np.eye(3)
# identity_arr = np.identity(3)
print(identity_arr)

# 👉🏻 7. np.full – Create array filled with a specific value
full_arr = np.full((3, 3), np.nan)
print(full_arr)

full_arr = np.full((2, 3), 13)
print(full_arr)

# =============== Indexing & Slicing =================

# 👉🏻 1D Array
arr = np.array([10, 20, 30, 40, 50])

print(arr[0] + arr[1])

print(arr[0])  # 10 → first element
print(arr[1])  # 20 → second element
print(arr[1:4])  # [20 30 40] → slice
print(arr[::2])  # [10 30 50] → every 2nd element
print(arr[::-1])  # [50 40 30 20 10] -> reverse
print(arr[1::2])  # [20 40]
print(arr[::-2])  # [50 30 10]
print(arr[:])  # [10 20 30 40 50]
print(arr[::])  # [10 20 30 40 50]

# 👉🏻 2D Array

arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D[0, 1])  # 2 -> row 0, col 1
print(arr2D[1, 2])  # 6 -> row 1, col 2

print(arr2D[:, :])  # entire array
print(arr2D[:])  # entire array
print(arr2D[::2])  # Every 2nd row
print(arr2D[::-1])  # Reverse Row wise
print(arr2D[:, ::2])  # Every 2nd column
print(arr2D[:, ::-1])  # reverse column wise

# Important
print(arr2D[::-1, ::-1])  # fully reverse

print(arr2D[:2])  # first 2 row
print(arr2D[::2])  # every 2nd row

print(arr2D[:, :2])  # first 2 column
print(arr2D[:, ::2])  # every 2nd column

print(arr2D[:2, :2])  # First 2 row and column
print(arr2D[::2, ::2])  # every 2nd row and column

print(arr2D[0, 1] + arr2D[1, 1])

# =============== Reshaping Arrays =================

# 1D -> 2D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.shape)  # (8,) → 1D
arr2D = arr.reshape(2, 4)
# arr2D = arr.reshape(4,2)
print(arr2D)
print(arr2D.shape)  # (2,4)

# Practice

# 1. Create arrays using:
#       np.zeros((3,3))
#       np.ones((2,4))
#       np.arange(5,20,3)
#       np.linspace(0,10,6)

print(np.zeros((3, 3)))
print(np.ones((2, 4)))
print(np.arange(5, 20, 3))
print(np.linspace(0, 10, 6))

# 2. Create 2D array: [[10,20,30],[40,50,60]]
#       Print first row, second column, submatrix arr[0:2,1:3]

D2 = np.array([[10, 20, 30], [40, 50, 60]])
print(f"First row :- {D2[:1]}")
print(f"Second column :- \n{D2[:, 1:2]}")
print(f"Sub matric :- \n{D2[0:2, 1:3]}")

# 3. Reshape 1D array [1,2,3,4,5,6] to 2D (2,3)
one = np.array([1, 2, 3, 4, 5, 6])
one = np.reshape(one, (2, 3))
print(one)

# =============== Flatten & Transpose =================

# Flattening converts an array of any dimension (2D, 3D, …) into a 1D array.
# By using ravel() & flatten()

arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D.flatten())
print(arr2D.ravel())
# ravel() -> returns a view (no new copy if possible)
# flatten() -> returns a new copy

# Transpose swaps the rows and columns of a 2D array.
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D.T)
