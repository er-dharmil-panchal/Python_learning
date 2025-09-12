"""
📌 NumPy – Step 8 (Working with Real Data)

This file covers:
    - Loading data from CSV/TXT files
    - Exploring dataset attributes
    - Handling missing values
    - Normalization & Standardization
    - Indexing & Conditional Selection
    - Practical Use cases
    - Quick Recap

📝 Summary:
    - NumPy allows you to efficiently load, explore, clean, and preprocess real-world datasets.
    - Handling missing values, scaling data, and selecting subsets are crucial for ML and data analysis workflows.
    - Key functions: np.loadtxt(), np.genfromtxt(), np.isnan(), np.nanmean(), np.where(), array slicing, and normalization/standardization formulas.
"""

import numpy as np

# Name,Math,Science,English
# John,78,82,900
# Alice,85,79,88
# # this is student data
# Mark,92,95,
# Sophia,88,,91
# David,75,80,85
# David,75,80,85


# =============== Loading Data =================
# np.loadtxt() -> Fast, Simple (Numeric Only)


# delimiter="," → separates values
# skiprows=1 → ignore header row
# usecols=(1,2,3) → pick specific columns
# dtype=float → force datatype
# comments = "#" -> detect comment and skip that for loading

# 👉🏻 np.loadtxt() :- only take numeric.

# data = np.loadtxt("student.csv",delimiter=",",skiprows=1,usecols=(1,2,3),dtype=float)
# np.loadtxt() expects every value to be numeric
# But Mark’s English mark is missing -> empty string ''

# 👉🏻 np.genfromtxt()
# here is the solution with genfromtxt.
# We must use np.genfromtxt() because it was made for real-world messy data.

data = np.genfromtxt('student.csv', delimiter=',', skip_header=1, usecols=(1, 2, 3), dtype=float, comments='#')
print(data)
print(data.shape)  # (6, 3)

# =============== Handling Missing Values =================
# Finding NaN

# We can check exactly which values are NaN using np.isnan():
print("NAN :- \n", np.isnan(data))
# True -> missing, False -> valid number

# 👉🏻 np.isnan() with np.where() - IMPORTANT

print(np.where(np.isnan(data)))
# (array([2, 3]), array([2, 1]))
# 👉🏻 here array([2, 3]) represents the rows of nan found, and [2,1] is column of nan
# 👉🏻 so correct pair we should imagine is first nan at data[(2,2)] and 2nd should be data[(3,1)]
print(f"first nan is at (2,2) :- {data[(2, 2)]}")  # nan
print(f"second nan is at (3,1) :- {data[(3, 1)]}")  # nan
print(data[np.where(np.isnan(data))])  # [nan nan]

# Confusion Alert
# Remember (array([2, 3]), array([2, 1])), this is seen normal indexing at first
# for indexing we use (), inside this, first index should row and other should column
# so first index is array([2,3]), means there is 2 nan at row 2 and 3, Now I think it should feel sorted

# 👉🏻 can also count NaN values
print(f"Count of the mission values :- {np.isnan(data).sum()}")  # 2

# Can also create array with nan
arr = np.array([1, 2, 3, 4, np.nan, 6, np.nan, 9, 10, 11, np.nan, np.nan])
print(np.isnan(arr).sum())  # 4

# sum with nan
print(np.sum(arr))  # nan ❌
print(np.nansum(arr))  # 46.0
print(np.nansum(data, axis=1))  # row wise  - [250. 252. 187. 179. 240.]
print(np.nansum(data, axis=0))  # column  wise  - [418. 336. 354.]
print(np.nansum(data))  # 1108.0 (total)
print(np.sum(data))  # nan ❌

# avg
print(np.mean(arr))  # nan ❌
print(np.nanmean(arr))  # 5.75  (nan will not count)
print(np.nanmean(data, axis=1))
print(np.nanmean(data, axis=0))

# std
print(np.nanstd(arr))  # 3.59687364248454

# 👉🏻 replace NaN with values.

clean = np.nan_to_num(arr, nan=13)  # Replace NaN with 13, But original array will not change
print(clean)  # [ 1.  2.  3.  4. 13.  6. 13.  9. 10. 11. 13. 13.]
print(arr)

clean = np.nan_to_num(arr, copy=False)
# If True (default), returns a new array. If False, modifies the original array in place.
# False - Memory efficient – avoids creating a new array (important for big datasets).
# convenient if you don’t need the original with nan.
print(clean)
print(arr)

# 👉🏻 With 2D arrays, you can remove any row containing nan:
arr = np.array([[78, 82, 90], [85, 79, 88], [92, 95, np.nan], [88, np.nan, 91]])
clean_rows = arr[~np.isnan(arr)]  # remove nan
print(clean_rows)
clean_rows = arr[~np.isnan(arr).any(axis=1)]
print(clean_rows)  # remove rows


# =============== np.take() – Pick elements by index =================

arr = np.array([10, 20, 30, 40, 50])
inds = [0, 2, 4]  # indices we wanna grab
picked = np.take(arr, inds)
print("Picked elements with np.take():", picked)  # [10 30 50]
# Wait, we can also do this with direct indexing
print("Picked elements with direct indexing:", arr[[0, 2, 4]])  # [10 30 50]


# 👉🏻 Why to use take(), if we can do same work with direct indexing ?
## 1) axis control
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Pick 1st and 3rd columns
print(np.take(arr2D, [0,2],axis=1))
# Doing the same with direct indexing is less clean:
print(arr2D[:,[0,2]])

## 2) Flattened Indexing
# By default, np.take() flattens the array before picking elements (if axis=None).

print(np.take(arr2D, [0, 4, 8]))        # start with 0 increase row wise
#direct indexing
# print(arr2D[[0, 2, 4]])         # IndexError: index 4 is out of bounds for axis 0 with size 3
# For “flattened” element access, np.take() is much simpler.

## 3) Mode Parameter (Extra Safety)
# "clip" → clips index to the valid range
# "wrap" → wraps around like modular arithmetic
# "raise" (default) → error if out of bounds
arr = np.array([10, 20, 30])
print(np.take(arr, [0, 4], mode='clip'))  # [10 30] → clipped to last valid index
print(np.take(arr, [0, 4], mode='wrap'))  # [10 20] → wrapped around (4 % 3 = 1 → index 1)

## 4) Performance (C-level Optimization)
# np.take() is implemented in C and optimized for bulk operations.
# In some scenarios (large arrays, complex indexing), it can be faster than fancy indexing because it avoids Python-level overhead.

## 5) Consistency in Data Cleaning
# np.take() integrates well with np.where() and np.isnan() workflows,   (just like i did)
# making it convenient for filling missing values or applying column-wise replacements.

# 👉🏻 Works for 2D arrays too (and higher dimensions).
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
# Both work, but np.take(..., axis=1) is explicit and scales better for higher dimensions.
# pick elements in flattened way
picked2D = np.take(arr2D, [0, 4, 8])
print("Picked from 2D flattened:", picked2D)  # [1 5 9]

# use np.take() with axis to be more controlled
picked_col = np.take(arr2D, [0, 2], axis=1)  # pick 1st & 3rd column
print("Picked columns:\n", picked_col)


# =============== Data Cleaning =================
# practical practice
arr = np.array([[78, 82, 90], [85, 79, 88], [92, 95, np.nan], [88, np.nan, 91]])

# Compute column means ignoring nan
col_mean = np.nanmean(arr, axis=0)
# Replace nan with column mean
inds = np.where(np.isnan(arr))
print(inds)  # (array([2, 3]), array([2, 1]))
arr[inds] = np.take(col_mean, inds[1])
print(arr)

# set the nan of the data from csv
np.nan_to_num(data, nan=0, copy=False)
print(data)

# we can do like delete nan with
# clean_data = np.unique(data, axis=0)
# like, in our data 2 rows are same.

_, idx = np.unique(data, axis=0, return_index=True)
unique_ordered_data = data[np.sort(idx)]
print(unique_ordered_data)

# filter invalid marks with 0 , or with avg
unique_ordered_data[(unique_ordered_data < 0) | (unique_ordered_data > 100)] = 0
print(unique_ordered_data)


# =============== Normalization & Standardisation =================

# ✅IMPORTANT ✅
# When you work with real-world data (like marks, heights, prices), the numbers can be on very different scales:
# marks - 0 to 100
# height - 1.6 to 1.8 (m)
# salary 25k to 80k

# 👉🏻now a ML algorithm like linear regression or any, tries to measure distance between these point
# for this data it should be sqrt((0.2)^2 + (55000)^2) = 55000
# Now we clearly see that this 55000 is dominated by the salary because 55000 >>> 0.2
# The algorithm will almost ignore height, because its contribution is tiny compared to salary.

# ✅ Solution → Scaling (Normalization & Standardization)

# 👉🏻 Normalization - This brings all values into [0, 1] range, so no feature can be "too big" compared to others.
# Formula :- x` = (x - np.min(x))/(np.max(x) - np.min(x))
height = np.array([1.6, 1.8, 1.2])
salary = np.array([25000, 80000, 50000])
h_norm = (height - np.min(height)) / (np.max(height) - np.min(height))
s_norm = (salary - np.min(salary)) / (np.max(salary) - np.min(salary))

print(f"Height norm: {h_norm}")         # [0.66666667 1.         0.        ]
print(f"Salary norm: {s_norm}")         # [0.         1.         0.45454545]

# normalization always preserves the order and pattern of the data.
# smallest -> became 0.00
# largest -> became 1.00
# between -> 0.67 or 0.45

# ✅ Normalization scales data between 0 and 1 while preserving the order, ensuring all features contribute fairly in ML models.

# 👉🏻 Standardisation
# Sometimes normalization (0→1) is not enough, especially if data is not 'uniformly distributed'.
# Standardisation makes data centered around 0 and scaled by its own variability.

# formula :- x` = (x-np.mean(x))/np.std(x)

height = np.array([150, 160, 170, 180, 190])
print("Mean(Without Standardisation):", np.mean(height))  # ~170
print("Std(Without Standardisation):", np.std(height))    # ~14
standardized_height = (height - np.mean(height)) / np.std(height)
print("After standardization:")
print("Mean:", np.mean(standardized_height))  # ~0
print("Std:", np.std(standardized_height))    # ~1
print("Standardized Data:", standardized_height)        # [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]


# =============== Indexing & Conditional Selection =================
# Select first 5 rows
first_5_rows = data[:5, :]
print("First 5 rows:\n", first_5_rows)

# Select second column
col2 = data[:, 1]
print("Second column:", col2)

# Conditional selection (values > 50)
high_values = data[data > 50]
print("Values > 50:", high_values)


# =============== Practical Use Cases =================
# Filter rows where Feature1 > 50
filtered_data = data[data[:, 0] > 50]
print("Filtered rows (Feature1>50):\n", filtered_data)

# Quick conditional labeling
labels = np.where(data[:, 1] > 75, 'High', 'Low')
print("Labels based on Feature2:", labels)

# Combine multiple steps: normalize + filter
normalized = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))
filtered_norm = normalized[normalized[:, 0] > 0.5]
print("Filtered normalized data:\n", filtered_norm)

"""
📌 Quick Recap
- Load data: np.loadtxt() (simple), np.genfromtxt() (handles NaN)
- Explore: shape, dtype, ndim, size
- Handle missing values: np.isnan(), np.nanmean(), np.where()
- Scale: normalization (0-1), standardization (mean=0, std=1)
- Indexing & selection: slicing, conditional selection
- Practical tips: Always explore & clean before analysis, normalize/standardize before ML, use conditional selection for feature filtering.
"""
