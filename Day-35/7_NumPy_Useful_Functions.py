"""
📌  NumPy – Step 7 (Useful Functions)

This file covers:
    - Unique elements
    - Sorting
    - Stacking Arrays
    - Splitting Arrays
    - Searching in NumPy
    - Practical examples with ML datasets
    - Quick Recap

📝 Summary:
    - NumPy has powerful utility functions to help with data manipulation, sorting, stacking, splitting, and searching arrays efficiently.
    - These functions are essential for data preprocessing, ML workflows, and array transformations.
    - np.unique(), np.sort(), np.argsort(), np.hstack(), np.vstack(), np.stack(), np.column_stack(), np.dstack(), np.concatenate(),
        np.split(), np.array_split(), np.hsplit(), np.vsplit(), np.where(), np.nonzero(), np.argwhere(), np.any(), np.all(), np.searchsorted() are key.
"""
import numpy as np

# =============== Unique elements =================
# np.unique() returns the "sorted unique elements" of an array. Very useful for removing duplicates or finding categories.
# NOTE:- np.unique() always sorts output

arr = np.array([2, 2, 5, 11, 2, 9, 11])
unique_arr = np.unique(arr)
print(unique_arr)

# You can also find how many times each unique element appears using return_counts=True
print(np.unique(arr, return_counts=True))  # (array([ 2,  5,  9, 11]), array([3, 1, 1, 2]))
# means 2 occur 3 time , 5 occur 1 time ....
# This is very useful in histograms, frequency tables, and class distributions.

# return_index=True → first occurrence index
uarr, index = np.unique(arr, return_index=True)
print(f"Unique elements in array: {uarr}, at index of : {index}")

# return_inverse=True → reconstruct original
unique_vals, inverse = np.unique(arr, return_inverse=True)
print(f"{unique_vals}")
print(f"{inverse}")
reconstructed_arr = unique_vals[inverse]
print(reconstructed_arr)
# This is useful when mapping original values to compact categories, e.g., converting labels to numeric indices in ML.

unique_vals, indices, counts = np.unique(arr, return_index=True, return_counts=True)
print(unique_vals)  # [ 2  5  9 11]
print(indices)  # [0 2 5 3]
print(counts)  # [3 1 1 2]

# Work with multidimensional arrays
arr2D = np.array([[1, 2, 3], [2, 3, 4], [2, 3, 4]])
unique_vals = np.unique(arr2D)
print(unique_vals)  # [1 2 3 4]

# To preserve rows or columns, use the axis parameter
unique_rows = np.unique(arr2D, axis=0)
print(unique_rows)

# Example :- Frequency counts for categorical data:
labels = np.array(['cat', 'dog', 'cat', 'bird', 'dog'])
unique_labels, counts = np.unique(labels, return_counts=True)
print(f"Unique labels: {unique_labels}, counts: {counts}")

# =============== Sorting =================
# np.sort() is a NumPy function that returns a sorted copy of an array.
# It does not change the original array unless you use the in-place .sort() method.
# Note that .sort() change the original array.

# 👉🏻 1-D
arr = np.array([5, 2, 4, 1, 3])
sorted_arr = np.sort(arr)
print(f"Sorted Array - {sorted_arr}")
print(f"Original Array - {arr}")

# in-place .sort()
arr.sort()
print(f"Original Array after using .sort() - {arr}")

# 👉🏻 2-D
arr2D = np.array([[3, 2, 1], [6, 0, 2]])
# a) Sort each row (axis=1) ( Default is always axis = 1)
sorted_rows = np.sort(arr2D, axis=1)
print(sorted_rows)
# b) Sort each column (axis=0)
sorted_rows = np.sort(arr2D, axis=0)
print(sorted_rows)

# 👉🏻 Flattened sort - Useful when you want all values sorted globally, ignoring rows/columns.
# Without axis, np.sort() flattens the array first:
print(np.sort(arr2D, axis=None))  # [0 1 2 2 3 6]
# remember if we just np.sort(arr2D) then it will give each column sorted, because default is axis = 1.

# 👉🏻 Sorting strings or objects
names = np.array(['John', 'Alice', 'Bob', 'arjun', 'bhishma', 'aman', 'bharat'])
sorted_names = np.sort(names)
print(sorted_names)
# Output: ['Alice' 'Bob' 'John' 'aman' 'arjun' 'bharat' 'bhishma']

# 👉🏻 Sorting boolean
arr = np.array([True, False, True])
print(np.sort(arr))

# 👉🏻 Sorting with argsort vs sort
# np.sort() → gives sorted values
# np.argsort() → gives indices that would sort the array
arr = np.array([50, 20, 30])
print(np.sort(arr))  # [20 30 50]
indices = np.argsort(arr)
print(indices)  # [1 2 0]
sorted_arr = arr[indices]
print(sorted_arr)  # [20 30 50]
# Use argsort() when you want to reorder another array according to sorting.

# reverse
indices_desc = np.argsort(arr)[::-1]  # reverse indices
print(indices_desc)  # [0 2 1]
arr_desc = arr[indices_desc]
print(arr_desc)  # [50 30 20]

# with 2-D
scores = np.array([[90, 80, 70], [60, 50, 40]])
# Sort each row
sorted_indices = np.argsort(scores, axis=1)
print(sorted_indices)

sorsorted_scores = np.take_along_axis(scores, sorted_indices, axis=1)
print(sorsorted_scores)

# 📌 Practical use

# 👉🏻 Rank data / find top values
scores = np.array([90, 75, 85, 100])
top_scores = np.sort(scores)[-2:]  # top 2 scores - [90 100]
print(top_scores)  # [90 100]
# better
top_scores = np.sort(scores)[::-1][:2]  # top 2 scores - [100 90]
# top_scores = np.sort(scores)[-2:][::-1]
print(top_scores)

# 👉🏻 sort the data with score
data = np.array([[90, 'Alice'], [70, 'Bob'], [85, 'Charlie']], dtype=object)
# Sort by score (column 0)
indices = np.argsort(data[:, 0].astype(int))[::-1]  # descending
sorted_data = data[indices]
print(sorted_data)
# Output:
# [[90 'Alice']
#  [85 'Charlie']
#  [70 'Bob']]


# =============== Stacking Arrays =================
# Stacking means combining multiple arrays along different axes.

# 👉🏻 np.hstack() – Horizontal Stack (side by side) (Arrays are joined along axis 1 (side by side))
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
hstacked = np.hstack((a, b))
print(hstacked)  # [1 2 3 4 5 6]

# 2-D
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.hstack((arr1, arr2)))
# [[1 2 5 6]
#  [3 4 7 8]]

# 👉🏻 np.vstack() – Vertical Stack (one on top of another)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
vstacked = np.vstack((a, b))
print(vstacked)
# [[1 2 3]
#  [4 5 6]]

# 2-D
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.vstack((arr1, arr2)))
# [[1 2 5 6]
#  [3 4 7 8]]

# 👉🏻 np.stack() – Stack along a new axis
# default is axis = 0
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked = np.stack((a, b), axis=1)
print(stacked)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
print(np.stack((a, b), axis=0))
# [[1 2 3]
#  [4 5 6]]

# axis=0 → stacked along first dimension
# axis=1 → stacked along second dimension


# Difference vs hstack/vstack:
# stack creates a new axis, while hstack and vstack just join existing axes.
print(np.vstack((arr1, arr2)).shape)  # (4, 2)
print(np.stack((arr1, arr2), axis=0).shape)  # (2, 2, 2)

# 👉🏻 np.column_stack() – Stack 1D arrays as columns (2D result)
# column_stack() as a shortcut for np.stack(..., axis=1) but only for 1D arrays.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
col_stacked = np.column_stack((a, b))
print(col_stacked)

# 👉🏻 np.row_stack() – Stack 1D arrays as rows - deprecated , use np.vstack

# 👉🏻 np.dstack() – Stack along depth (axis=2)
# dstack = depth stack → adds a third dimension
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
depth_stacked = np.dstack((a, b))
print(depth_stacked)

print("\n\n\n\n")
# 👉🏻 np.concatenate() – General-purpose join (no new axis)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
concat = np.concatenate((a, b), axis=0)  # join rows
print(concat)
concat = np.concatenate((a, b), axis=1)  # join columns
print(concat)

# =============== Splitting Arrays =================
# Splitting arrays means breaking a single array into multiple sub-arrays.
# This is very useful in data preprocessing, batch processing, or dividing data for training/testing in ML.

# 👉🏻 np.split() – Split into equal parts - The array must be divisible evenly by the number of splits.
arr = np.array([1, 2, 3, 4, 5, 6])
subarrays = np.split(arr, 3)  # split into 3 equal parts
print(subarrays)  # [array([1, 2]), array([3, 4]), array([5, 6])]

# 👉🏻 np.array_split() – Flexible split (unequal sizes) - Works even if the array cannot be divided equally.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
subarrays = np.array_split(arr, 3)
print(subarrays)  # [array([1, 2, 3]), array([4, 5]), array([6, 7])]
print(subarrays[0])
print(subarrays[1])
print(subarrays[2])

# 👉🏻 np.hsplit() – Split horizontally (columns) in 2D arrays
arr2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
subarrays = np.hsplit(arr2D,
                      2)  # split into 2 column-wise subarrays - The array must be divisible evenly by the number of splits.
print(subarrays)

# use this for not evenly dived array length
arr2D1 = np.array([[1, 2, 3, 4, 10], [5, 6, 7, 8, 11]])
print(np.hsplit(arr2D1, [2]))

# 👉🏻 np.vsplit() - Split vertically (rows) in 2D arrays
subarrays = np.vsplit(arr2D,
                      2)  # split into 2 row-wise subarrays - The array must be divisible evenly by the number of splits.
print(subarrays)

# use this for not evenly dived array length
arr2D = np.array([[1, 2, 3, 4, 10], [5, 6, 7, 8, 11]])
print(np.hsplit(arr2D, [2]))

# 📌 Practical example

# Splitting dataset for training/testing
data = np.arange(10)
train, test = np.split(data, [7])  # first 7 for train, remaining 3 for test
print(train)  # [0 1 2 3 4 5 6]
print(test)  # [7 8 9]

"""
# Combine splitting + stacking to divide and recombine datasets easily for ML workflows.
| Function           | Axis / Behavior                | Notes                                       |
| ------------------ | ------------------------------ | ------------------------------------------- |
| `np.split()`       | 0 by default for 1D arrays     | Must be divisible evenly                    |
| `np.array_split()` | 0 by default for 1D arrays     | Unequal splits allowed                      |
| `np.hsplit()`      | axis=1 (columns) for 2D arrays | Must divide columns evenly (or use indices) |
| `np.vsplit()`      | axis=0 (rows) for 2D arrays    | Must divide rows evenly (or use indices)    |

"""


# =============== Searching in NumPy =================

# 👉🏻 np.where() – Conditional Search
arr = np.array([10, 20, 30, 40, 50])
# Get indices where condition is True
indices = np.where(arr > 25)
print(indices)  # (array([2, 3, 4]),)
print(arr[indices])  # [30 40 50]

# use as if-else
result = np.where(arr > 25, "Big", "Small")
print(result)  # ['Small' 'Small' 'Big' 'Big' 'Big']

# 👉🏻 np.nonzero() – Indices of Non-Zero Elements
arr = np.array([0, 5, 0, 8, 9])
indices = np.nonzero(arr)
print(indices)  # (array([1, 3, 4]),)
print(arr[indices])  # [5 8 9]

# 👉🏻 np.argwhere() – Returns Indices as 2D array
arr = np.array([10, 20, 30, 40, 50])
indices = np.argwhere(arr > 20)
print(indices)
# [[2]
#  [3]
#  [4]]
print(arr[indices])
# [[30]
#  [40]
#  [50]]

# 👉🏻 np.any() & np.all() – Check conditions
arr = np.array([1, 2, 3, 0])
print(np.any(arr > 2))  # True  (at least one element > 2)
print(np.all(arr > 0))  # False (not all elements > 0)

# 👉🏻 np.searchsorted() – Search in Sorted Array
arr = np.array([10, 20, 30, 40, 50])
idx = np.searchsorted(arr, 35)
print(idx)  # 3 (index where 35 should go)
idx = np.searchsorted(arr, [1, 22, 32])
print(idx)  # [0 2 3]

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # (array([3, 5, 6]),)
x = np.where(arr % 2 == 0)
print(x)  # (array([1, 3, 5, 6]),)

arr = np.array([4, 9, 6, 7, 8, 9, 4])  # it will be [4, 4, 6, 7, 8, 9, 9]
print(np.searchsorted(arr, 4))  # 0
print(np.searchsorted(arr, 4, side='right'))  # 1
x = np.searchsorted(arr, 9)
print(x)
x = np.searchsorted(arr, 9, side='left')
print(x)
x = np.searchsorted(arr, 9, side='right')
print(x)

"""
📌 Quick Recap
- Unique elements → np.unique(), return_counts, return_index, return_inverse
- Sorting → np.sort(), np.argsort(), axis, flattened sort, strings, booleans
- Stacking → np.hstack(), np.vstack(), np.stack(), np.column_stack(), np.dstack(), np.concatenate()
- Splitting → np.split(), np.array_split(), np.hsplit(), np.vsplit()
- Searching → np.where(), np.nonzero(), np.argwhere(), np.any(), np.all(), np.searchsorted()
- Practical Tips:
- Use np.unique() for categories or frequency counts
- np.argsort() to reorder related arrays
- np.stack() creates new axis, hstack/vstack do not
- np.split/array_split to divide datasets for ML
- np.searchsorted() assumes sorted array for insertion index
"""
