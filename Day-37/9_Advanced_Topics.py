"""
📌 NumPy – Step 9 (Advanced Topics)

This file covers:
    - Broadcasting
    - Vectorization
    - Memory Layout: Views vs Copies
    - Performance Comparison: NumPy vs Python Lists
    - Structured Arrays
    - Iterating with nditer
    - Trigonometric & Mathematical Functions
    - Percentiles, Correlation, Histogram
    - Quick Recap

📝 Summary:
    - Broadcasting allows operations on arrays of different shapes without explicit loops.
    - Vectorization enables loop-free, fast numerical operations using NumPy.
    - Views vs Copies determine whether array operations affect the original data.
    - NumPy arrays are faster than Python lists for numerical computations.
    - Structured arrays support heterogeneous data with field names.
    - nditer provides flexible iteration over arrays of any dimension, with broadcasting support.
    - NumPy has built-in support for trigonometric, statistical, and aggregation functions.
"""
import time
import numpy as np

# =============== Broadcasting =================
# It’s NumPy’s way of performing operations on arrays of different shapes without explicit loops.
# When two arrays are combined (addition, subtraction, etc.), NumPy compares their shapes from right to left (last dimension -> first).
# ✅ Compatible if
#   They are equal, OR
#   One of them is 1 (it will “stretch” to match the other)
# ❌ Incompatible if
#   Neither is 1, and they are not equal → NumPy throws an error.

# ->>> Examples

# Scalar + Array (Simplest Case)
a = np.array([1, 2, 3, 4, 5])
print(a + 5)  # [ 6  7  8  9 10]
# Scalar is treated as shape (1,), stretches to (3,).

# for 2-D
matrix = np.array([[1, 2, 3], [4, 5, 6]])  # shape = (2, 3)
row = np.array([10, 20])  # shape = (2,)

# 📝 Broadcasting explanation:
# matrix.shape = (2, 3)
# row.shape    = (2,) → NumPy right-aligns → becomes (1, 2)
#
# Compare dimensions from right:
#   - Last dim: 3 vs 2 → ❌ Not equal & not 1 → INCOMPATIBLE
#
# So this will raise:
# ValueError: operands could not be broadcast together with shapes (2,3) (2,)

# Uncomment to see the error:
# print(matrix + row)

# ✅ FIX: reshape row to (2,1) so it broadcasts along columns
row_fixed = row.reshape(2, 1)  # shape = (2, 1)
print(matrix + row_fixed)

# NOTE :- simple trick to understand
# 🔥 We just have to match this array's row or column with the other array, and the other dimension should be 1 so it aligns perfectly for the operation

matrix = np.array([[1, 2, 3], [4, 5, 6]])  # shape = (2, 3)
row = np.array([10, 20, 30])  # shape = (3,)

# 📝 Broadcasting explanation:
# matrix.shape = (2, 3)
# row.shape    = (3,) → NumPy right-aligns → becomes (1, 3)
#
# Compare dimensions from right:
#   - Last dim: 3 vs 3 ✅ Match
#   - First dim: 2 vs 1 ✅ 1 can be stretched to 2
#
# ✅ Compatible → row is broadcast to match matrix shape (2, 3)
print(matrix + row)

# Column + Row (Classic 2D Broadcasting)
col = np.array([[1], [2], [3]])  # shape (3,1)
row = np.array([10, 20, 30, 40])  # shape (4,)
print(row + col)
# if you know little matrix then it will be too easy to measure that this is valid or not

# without broadcasting we have to run nested loop for 2 array then have to do operation, like this
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # shape (3, 4)

row = np.array([10, 20, 30, 40])  # shape (4,)
result = np.zeros((3, 4))
for i in range(3):
    for j in range(4):
        result[i, j] = matrix[i, j] + row[j]
print("Result using loops:\n", result)

# with broadcasting
result_broadcast = matrix + row
print("\nResult using broadcasting:\n", result_broadcast)

# =============== Vectorization =================
# In Python, loops are slow because they execute in the interpreter.
# NumPy operations are implemented in C under the hood → much faster.

# Two arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Using loops
result_loop = np.zeros(5)
for i in range(5):
    result_loop[i] = a[i] + b[i]

# Vectorized
result_vectorized = a + b

print(result_loop)  # [11 22 33 44 55]
print(result_vectorized)  # [11 22 33 44 55]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row = np.array([10, 20, 30])
result = matrix + row  # row is broadcast automatically
print(result)

# Operations
# Sample array
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("Arithmetic:")
print("Addition:", a + b)  # [11 22 33 44 55]
print("Subtraction:", b - a)  # [9 18 27 36 45]
print("Multiplication:", a * b)  # [10 40 90 160 250]
print("Division:", b / a)  # [10. 10. 10. 10. 10.]
print("Modulus:", b % a)  # [0 0 0 0 0]
print("Power:", a ** 2)  # [1 4 9 16 25]

print("\nComparison:")
print("a > 3:", a > 3)  # [False False False  True  True]
print("b <= 30:", b <= 30)  # [ True  True  True False False]
print("a == 2:", a == 2)  # [False  True False False False]

print("\nAggregation:")
print("Sum of a:", np.sum(a))  # 15
print("Mean of b:", np.mean(b))  # 30.0
print("Max of a:", np.max(a))  # 5
print("Min of b:", np.min(b))  # 10

print("\nMathematical functions:")
print("Square root of a:", np.sqrt(a))  # [1. 1.414 1.732 ...]
print("Exponential of a:", np.exp(a))  # [2.718 7.389 ...]
print("Log of b:", np.log(b))  # [2.30 2.99 ...]
print("Sin of a:", np.sin(a))  # [0.841 0.909 ...]

print("\nConditional selection:")
# If a > 3, pick from b, else pick from a
result = np.where(a > 3, b, a)
print(result)  # [1 2 3 40 50]

# Benefits of Vectorization
# Speed: Operations happen in compiled C, not Python loops.
# Readability: No nested loops, fewer lines of code.
# Safety: Avoids off-by-one or index errors.
# Works with broadcasting: Can operate on arrays of different shapes seamlessly.

# Broadcasting = shape alignment
# Vectorization = loop-free operations


# =============== Memory Layout: Views vs Copies =================
# NumPy arrays can share memory or make copies depending on operations:

# 👉🏻 Views (No Copy)
# Some operations do not copy data, just create a new view of the same array.
# Changing the view changes the original array.

# Slicing creates a view
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]  # slicing creates a view
b[0] = 100
print(a)  # [  1 100   3   4   5] -> original changed
print(b)  # [100   3   4]

# Reshape creates a view (usually)
a = np.arange(6)  # [0 1 2 3 4 5]
b = a.reshape(2, 3)  # 2x3 array
b[0, 0] = 100
print(a)  # [100 1 2 3 4 5] -> original affected

# 👉🏻 Copies
# A copy is a completely new array in memory.
# Changing the copy does not affect the original array.
a = np.array([1, 2, 3, 4, 5])
b = a[1:4].copy()  # explicit copy
b[0] = 200
print("Copy:", b)  # [200 3 4]
print("Original:", a)  # [1 2 3 4 5] → original unchanged

# Avoid accidental changes: If you modify a view thinking it’s a copy, you can unintentionally change the original array.
# Views are faster and memory-efficient (no extra memory).
# Copies use extra memory.

# Detecting Views vs Copies
a = np.arange(5)
b = a[1:4]
print(np.may_share_memory(a, b))  # True -> view

# =============== Performance Comparison: NumPy vs Python Lists =================
# Python lists are flexible but slow for numerical operations because:
#   Each element is a Python object -> more memory overhead.
#   Operations are executed in Python loops -> interpreted, not compiled.
# NumPy arrays are contiguous in memory and operations are implemented in fast C code -> huge speed advantage.

# Example, add 2 lists
size = 1_000_000
lst1 = list(range(size))
lst2 = list(range(size))

start = time.time()
result = [x + y for x, y in zip(lst1, lst2)]
end = time.time()
print("Python list time:", end - start)  # 0.038

# Using NumPy arrays (vectorized)

arr1 = np.arange(size)
arr2 = np.arange(size)
start = time.time()
result = arr1 + arr2  # vectorized + broadcasting
end = time.time()
print("NumPy array time:", end - start)  # 0.010
"""
| Operation                   | Python list                | NumPy array                |
| --------------------------- | -------------------------- | -------------------------- |
| Element-wise addition       | Slow (loop)                | Fast (vectorized)          |
| Multiplication              | Slow                       | Fast                       |
| Aggregation (`sum`, `mean`) | Slow                       | Fast (`np.sum`, `np.mean`) |
| Mathematical functions      | Slow (`math.sqrt` in loop) | Fast (`np.sqrt`, `np.log`) |
"""

# =============== Structured Arrays =================
# Structured arrays allow you to store heterogeneous data (different types) in a single NumPy array, similar to a table or database row.
data = np.array([(1, 'Alice', 20.5), (2, 'Bob', 30.2)], dtype=[('id', 'i4'), ('name', 'U10'), ('score', 'f4')])
"""
Some data types I found relevant for this topic.
| Code | Bytes | Type         | Example      | Notes                                |
| ---- | ----- | ------------ | ------------ | ------------------------------------ |
| i1   | 1     | Signed int   | -128 → 127   | 8-bit signed integer                 |
| i2   | 2     | Signed int   | -32k → 32k   | 16-bit signed integer                |
| i4   | 4     | Signed int   | -2B → 2B     | 32-bit signed integer (most common)  |
| i8   | 8     | Signed int   | Very large   | 64-bit signed integer                |
| u1   | 1     | Unsigned int | 0 → 255      | 8-bit unsigned integer               |
| u2   | 2     | Unsigned int | 0 → 65k      | 16-bit unsigned integer              |
| u4   | 4     | Unsigned int | 0 → 4B       | 32-bit unsigned integer              |
| u8   | 8     | Unsigned int | Very large   | 64-bit unsigned integer              |
| f2   | 2     | Float        | 1.5          | Half-precision float (rare)          |
| f4   | 4     | Float        | 3.14         | Single-precision float               |
| f8   | 8     | Float        | 3.141592     | Double-precision float (most common) |
| f16  | 16    | Float        | Very precise | Quad-precision float (rare)          |
| c8   | 8     | Complex      | 1+2j         | 4-byte real + 4-byte imag            |
| c16  | 16    | Complex      | 1+2j         | 8-byte real + 8-byte imag            |
| c32  | 32    | Complex      | Very large   | 16-byte real + 16-byte imag          |
| b1   | 1     | Boolean      | True / False | 1-byte boolean                       |
| S10  | 10    | Byte String  | b'hello'     | Fixed-length byte string             |
| U10  | 10    | Unicode      | 'hello'      | Fixed-length Unicode string          |
"""

# Accessing Fields
print(data['id'])  # [1 2]
print(data['name'])  # ['Alice' 'Bob']
print(data['score'])  # [20.5 30.2]

# Modifying Data
data['score'][1] = 35.0
print(data)
# [(1, 'Alice', 20.5) (2, 'Bob', 35.0)]

# Boolean Indexing with Structured Arrays
high_scores = data[data['score'] > 25]
print(high_scores)

# =============== Iterating =================
# It’s faster and cleaner than using nested loops for arrays of any dimension.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Basic iteration
for x in np.nditer(arr):
    print(x, end=" ")

# Modifying array values - To modify values, use op_flags=['readwrite'].
for x in np.nditer(arr, op_flags=['readwrite']):
    x[...] = x * 2  # multiply each element by 2
print("\n", arr)

# Iterating in a specific order (C or Fortran)
# NumPy arrays can be stored in row-major (C-order) or column-major (Fortran-order).
arr = np.array([[1, 2], [3, 4]])

print("C order:")
for x in np.nditer(arr, order='C'):
    print(x, end=" ")  # 1 2 3 4

print("\nFortran order:")
for x in np.nditer(arr, order='F'):
    print(x, end=" ")  # 1 3 2 4

# Iterating with broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])

b = np.array([10, 20, 30])

for x, y in np.nditer([arr, b]):
    print(x, "+", y, "=", x + y)

# Benefits of nditer:
# Works for any number of dimensions.
# Faster than nested Python loops.
# Can modify values in-place.
# Can combine multiple arrays and support broadcasting.
# Can choose iteration order (C vs F).


# some Trigonometric functions
# - np.sin(), np.cos(), np.tan() : Trigonometric functions.
# - np.arcsin(), np.arccos(), np.arctan() : Inverse trigonometric functions.
# - np.deg2rad(), np.rad2deg() : Convert degrees to radians and vice versa.
array = np.array([1, 2, 3, 4, 5])
sin_array = np.sin(array)
print(sin_array)
cos_array = np.cos(array)
print(cos_array)
tan_array = np.tan(array)
print(tan_array)

# np.trunc() : Truncate decimal part, keep integer part.
truncated_array = np.trunc(array)
print(truncated_array)

# np.percentile() : Percentile value in the array.
percentile_0 = np.percentile(array, 0)
percentile_25 = np.percentile(array, 25)
percentile_50 = np.percentile(array, 50)
percentile_75 = np.percentile(array, 75)
percentile_80 = np.percentile(array, 80)
print("0th Percentile (np.percentile) = ", percentile_0)  # 1.0
print("25th Percentile (np.percentile) = ", percentile_25)  # 2.0
print("50th Percentile (np.percentile) = ", percentile_50)  # 3.0
print("75th Percentile (np.percentile) = ", percentile_75)  # 4.0
print("80th Percentile (np.percentile) = ", percentile_80)  # 4.2

# np.corrcoef() : Correlation coefficient matrix.
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([5, 4, 3, 2, 1])
correlation_matrix = np.corrcoef(data1, data2)
print("Correlation coefficient matrix (np.corrcoef) = \n", correlation_matrix)

# np.histogram() : Histogram of array elements.
# bins → Number of intervals (or you can give a list of bin edges)
# hist → counts of values in each bin
hist, bin_edges = np.histogram(array, bins=4)
print("Histogram (np.histogram) = ", hist)
print("Bin edges (np.histogram) = ", bin_edges)

"""
📌 Quick Recap

- Broadcasting: operations on arrays of different shapes without explicit loops.
- Vectorization: loop-free, fast numerical operations using NumPy.
- Views vs Copies: determine whether array operations affect the original data.
- NumPy vs Python Lists: arrays are faster than Python lists for numerical computations.
- Structured Arrays: support heterogeneous data with field names.
- Iterating with nditer: flexible iteration over arrays of any dimension, with broadcasting support.
- Trigonometric & Mathematical Functions: np.sin(), np.cos(), np.tan(), np.sqrt(), np.exp(), np.log(), np.trunc().
- Percentiles, Correlation, Histogram: np.percentile(), np.corrcoef(), np.histogram().
- Practical Tips:
    - Use broadcasting to avoid explicit loops.
    - Vectorize operations for speed and readability.
    - Be aware of views vs copies to avoid unintentional modifications.
    - Use structured arrays for heterogeneous data.
    - Use nditer for efficient multi-dimensional iteration.
    - Utilize built-in math, trigonometric, and statistical functions.
"""