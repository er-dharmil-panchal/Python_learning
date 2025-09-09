"""
📌 Step 3 – NumPy Array Operations & Data Types

This file covers:
1. Arithmetic operations (add, subtract, multiply, divide)
2. Broadcasting rules
3. Universal functions (np.sqrt, np.exp, np.log, etc.)
4. Aggregations (np.sum, np.mean, np.max, np.min, np.std)
5. NumPy Data Types (i, u, b, f, c, m, M, O, S, U, V)
6. Changing data type using .astype()
"""

# =============== Import NumPy =================
import numpy as np

# =============== Arithmetic Operations =================
arr1 = np.array([10, 20, 30, 40], dtype=int)
arr2 = np.array([1, 2, 3, 4], dtype=float)

# Addition
result = arr1 + arr2
print("Addition:", result, result.dtype)  # [11. 22. 33. 44.] float64

# Subtraction
result = arr1 - arr2
print("Subtraction:", result, result.dtype)  # [ 9. 18. 27. 36.] float64

# Multiplication
result = arr1 * arr2
print("Multiplication:", result, result.dtype)  # [10. 40. 90. 160.] float64

# Division
result = arr1 / arr2
print("Division:", result, result.dtype)  # [10. 10. 10. 10.] float64

# =============== Broadcasting Rules =================
arr1 = np.array([1, 2, 3], dtype=int)
arr2 = 10  # scalar
result = arr1 + arr2
print("Broadcasting with scalar:", result, result.dtype)  # [11 12 13] int64

# =============== Universal Functions (ufuncs) =================
arr = np.array([1, 4, 9, 16])

print("Square Root:", np.sqrt(arr))  # [1. 2. 3. 4.]
print("Exponential:", np.exp(arr))   # [2.718..., 54.598..., 8103.08..., 8.8861e6...]
print("Natural Log:", np.log(arr))   # [0. 1.386 2.197 2.772]

# =============== Aggregations =================
arr = np.array([1, 2, 3, 4, 5])

print("Sum:", np.sum(arr))    # 15
print("Mean:", np.mean(arr))  # 3.0
print("Max:", np.max(arr))    # 5
print("Min:", np.min(arr))    # 1
print("Standard Deviation:", np.std(arr))  # 1.4142...
# The standard deviation measures how much the numbers in an array deviate from the mean.

# =============== Data Types =================
"""
NumPy has some extra data types. 
Refer to data types with one character, like:
    i - integer
    u - unsigned integer
    b - boolean
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string (byte string)
    U - unicode string
    V - void (raw memory block)
"""

# i - integer (signed)
arr_i = np.array([1, 2, 3], dtype='i')
print("Integer:", arr_i, arr_i.dtype)

# u - unsigned integer (cannot be negative)
arr_u = np.array([1, 2, 3], dtype='u4')
print("Unsigned Integer:", arr_u, arr_u.dtype)

# b - boolean
arr_b = np.array([True, False, True], dtype='b')
print("Boolean:", arr_b, arr_b.dtype)

# f - float
arr_f = np.array([1.5, 2.3, 3.7], dtype='f')
print("Float:", arr_f, arr_f.dtype)

# c - complex float
arr_c = np.array([1+2j, 3+4j], dtype='c')
print("Complex Float:", arr_c, arr_c.dtype)

# m - timedelta
arr_m = np.array(['2', '5'], dtype='timedelta64[D]')  # D → days
print("Timedelta:", arr_m, arr_m.dtype)

# M - datetime
arr_M = np.array(['2025-09-09', '2025-12-31'], dtype='M')
print("Datetime:", arr_M, arr_M.dtype)

# O - object (can store any Python object)
arr_O = np.array([1, "hello", [1, 2]], dtype='O')
print("Object:", arr_O, arr_O.dtype)

# S - string (byte string)
arr_S = np.array([b'apple', b'banana'], dtype='S')
print("Byte String:", arr_S, arr_S.dtype)

# U - unicode string
arr_U = np.array(['apple', 'banana'], dtype='U')
print("Unicode String:", arr_U, arr_U.dtype)

# V - void (raw fixed memory block)
# arr_V = np.array([1, 2, 3], dtype='V8')
# print("Void:", arr_V, arr_V.dtype)

# =============== Changing Data Type =================
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print("Float → Integer:", newarr, newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print("Float → Integer:", newarr, newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print("Integer → Boolean:", newarr, newarr.dtype)

# =============== Practice Task =================
"""
1. Create two arrays arr1=[5,10,15] and arr2=[2,4,6], perform all arithmetic operations.
2. Apply universal functions (sqrt, log, exp) on an array [4, 16, 25].
3. Create arrays with different data types (int, float, boolean, string, datetime).
4. Convert float array [1.2, 3.4, 5.6] to integer and boolean using .astype()
5. Experiment with broadcasting: add a scalar 5 to an array [1,2,3,4].
"""
