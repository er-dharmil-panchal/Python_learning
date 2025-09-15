"""
📌 Pandas – Step 1 (Introduction to Pandas)

This file covers:
    - What is Pandas & why use it
    - Pandas Data Structures (Series & DataFrame)
    - Creating Series (list, dict, scalar)
    - Series attributes & operations
    - Creating DataFrames (dict of lists, list of lists, NumPy array)
    - Inspecting DataFrames
    - Loading & Saving CSV/JSON files
    - Quick Recap

📝 Summary:
    - Pandas is built on top of NumPy, optimized for data manipulation.
    - Provides Series (1D) & DataFrame (2D) for structured data handling.
    - Can work with CSV, JSON, Excel seamlessly.
    - Powerful, easy-to-use API for analysis, cleaning, and exploration.
"""

import numpy as np
import pandas as pd

print(pd.__version__)  # 2.3.2

# =====================================================
# =============== DATA STRUCTURES =====================
# =====================================================

# =====================================================
# =============== Series — 1D object ==================
# =====================================================
# A Series is a one-dimensional labeled array that can hold any data type: integers, floats, strings, or even Python objects.
# Each element in the Series has a unique label called an index.
# Mostly use to track change and pattern over the time.

# ---------- Creating Series with different data types ----------
# From list
s = pd.Series([10, 20, 30, 40])
print(f"From list without indexing \n{s}")

s.index = ['a', 'b', 'c', 'd']
# OR -> s = pd.Series([10,20,30,40], index = ['a','b','c','d'])
print(f"From list with indexing \n{s}")

# From Dictionary
s2 = pd.Series({'a': 12, 'b': 13, 'c': 14, 'd': 15})
print(f"From dict \n{s2}")

# From Scalar (Broadcasted)
s3 = pd.Series(10, index=[1, 2, 3, 4])
print(f"From Scalar \n{s3}")

# ---------- Key Method and attribute ----------
print(f"Index {s3.index}")
print(f"Values {s3.values}")
print(f"Data type {s3.dtype}")
print(f"First 2 Row \n{s3.head(2)}")
# print(f"First 2 Row \n{s3[:2]}")
print(f"last 2 Row \n{s3.tail(2)}")

# ---------- Vectorized ops ----------
print(s3 * 2)

# ---------- Alignment: arithmetic aligns by index ----------
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
print(f"Sum of 2 Series with same number of index (Not same index) \n", s1 + s2)

# =====================================================
# =============== DataFrame — the 2D table ============
# =====================================================
# DataFrame is a two-dimensional data structer in pandas that are simpler to table in database
# Contains of Rows and columns
# here rows have indices (labels), and columns have name (labels).

# ---------- Creating DataFrame ----------
# 1) From Dictionary of Lists. (Most Common)
s1 = pd.DataFrame({"Name ": ["Dharmil", "Nihar", "Ansh"], "Age": [18, 19, 19]}, index=[1, 2, 3])
print(s1)

# 2) List of Lists.
s2 = pd.DataFrame(
    [["Dharmil", 18, "Ahmedabad"], ["Hani", 19, "Ahmedabad"], ["Dax", 19, "Ahmedabad"]],
    [1, 2, 3],
    columns=["Name", "Age", "City"]
)
print(s2)

# 3) From NumPy Array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(arr, columns=["c1", "c2", "c3"], index=[1, 2]))

# ---------- Inspecting a DataFrame ----------
print(f"\n\nFirst 2 rows \n{s2.head(2)}")  # first 5 rows
print(f"Last 2 rows \n{s2.tail(2)}")  # last 5 rows
print(f"Shape {s2.shape}")  # (n_rows, n_cols)
print(f"Columns {s2.columns}")  # Index of column names
print(f"Index {s2.index}")  # Index (row labels)
print(f"Information of the Data Frame {s2.info()}")  # types, non-null counts
print(f"Summary stats for numeric columns \n{s2.describe()}")  # summary stats for numeric columns
print(f"Data type \n{s2.dtypes}")  # dtype per column

# =====================================================
# =============== Loading/Saving data from CSV =========
# =====================================================
data = pd.read_csv("student.csv")
print("Fetching data from CSV file \n", data)

# ---------- Saving ----------
# data.to_csv("student.csv")
# Here one problem occur if you see the data there is indexing which we don't want in out csv file
data.to_csv("student.csv", index=False)

# =====================================================
# =============== Loading/Saving data from JSON ========
# =====================================================
data = pd.read_json("User.json")
print("\nFetching data from JSON file \n", data)

# ---------- Saving ----------
data.to_json("User.json")

# =====================================================
# ==================== QUICK RECAP ====================
# =====================================================
"""
📝 Quick Recap:
- Pandas is built on top of NumPy for easy data manipulation.
- Series → 1D labeled data (like a single column).
- DataFrame → 2D table with rows & columns.
- Series creation → from list, dict, scalar.
- Series methods → head(), tail(), index, values, dtype.
- DataFrame creation → dict of lists, list of lists, NumPy array.
- DataFrame inspection → head(), tail(), shape, columns, index, info(), describe().
- CSV/JSON → read_csv(), to_csv(index=False), read_json(), to_json().
"""
