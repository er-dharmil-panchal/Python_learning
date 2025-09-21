"""
📌 Pandas – Step 7 (Apply & Transform)
    - Real-world data often needs custom calculations or transformations that go beyond built-in functions.
    - apply / map / applymap let you run your own logic on Series or DataFrame.
    - transform lets you broadcast group-level calculations back to rows.

    This file covers:
    - .apply() → apply function row-wise/column-wise
    - .map() → apply function element-wise to Series
    - .applymap() → apply function element-wise to entire DataFrame
    - .transform() → group-wise transform (same shape as input)
    - Differences between apply, map, applymap, transform
    - Using lambda functions and custom functions
    - Vectorization vs. apply (performance consideration)

📝 Summary:
    - apply() → flexible; works on Series (element-wise) and DataFrames (row/column-wise)
    - map() → element-wise Series transform; accepts function, dict, or Series
    - applymap() → element-wise DataFrame transform; function called per cell
    - transform() → group-wise calculation broadcasted to original shape; used with groupby
    - Prefer vectorized operations over apply for performance

"""

import pandas as pd
import numpy as np

# =====================================================
# =============== SAMPLE DATA =========================
# =====================================================

df = pd.DataFrame({
    "name": ["Amit", "Bela", "Chetan", "Deep"],
    "math": [88, 92, 85, 70],
    "science": [90, 95, 80, 75],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"]
})

print("\n👉🏻 Original DataFrame")
print(df)

# =====================================================
# ==================== .apply() =======================
# =====================================================

# .apply() can be used on:
#   1) Series (1D) → function gets scalar
#   2) DataFrame (2D) → function gets Series per row/column

# Column-wise apply (default axis=0)
print("\n👉🏻 Column-wise apply → mean of each numeric column")
print(df[["math","science"]].apply(np.mean))

# Row-wise apply (axis=1)
print("\n👉🏻 Row-wise apply → total marks per student")
df["total"] = df[["math","science"]].apply(lambda row: row["math"] + row["science"], axis=1)
print(df)

# Apply with custom function
def grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    else: return "C"

print("\n👉🏻 Applying custom function to Series (math column)")
df["math_grade"] = df["math"].apply(grade)
print(df)

# =====================================================
# ===================== .map() ========================
# =====================================================

# .map() works only on Series and is element-wise
print("\n👉🏻 Using map() to transform city names to uppercase")
df["city_upper"] = df["city"].map(str.upper)
print(df)

# Map can also accept dict for mapping
city_map = {"Delhi": "DL", "Mumbai": "MB", "Pune": "PN"}
print("\n👉🏻 Using map() with dict to map city codes")
df["city_code"] = df["city"].map(city_map)
print(df)

# =====================================================
# ================== .applymap() ======================
# =====================================================

# applymap is only for DataFrame → element-wise transformation
print("\n👉🏻 Using applymap to add 5 marks to numeric columns")
df_num = df[["math","science"]]
print(df_num.applymap(lambda x: x+5))

# =====================================================
# ================== .transform() =====================
# =====================================================

# transform is often used with groupby to broadcast group result back to original rows
print("\n👉🏻 Using transform with groupby (group mean per city)")
df["city_math_mean"] = df.groupby("city")["math"].transform("mean")
print(df)

# Custom transform function
print("\n👉🏻 Custom transform: subtract city mean from math")
df["math_diff_from_city_avg"] = df["math"] - df.groupby("city")["math"].transform("mean")
print(df)

# =====================================================
# ========== apply vs map vs applymap vs transform =====
# =====================================================

"""
🔑 Key Differences:

* apply():
    - Works on DataFrame (row-wise / column-wise)
    - Works on Series (element-wise)
    - Can return scalar or Series/DataFrame
    - More flexible but slower for large data (use vectorized ops if possible)

* map():
    - Works only on Series
    - Element-wise transformation
    - Accepts function, dict, or Series
    - Fast for element-wise replacement

* applymap():
    - Works only on DataFrame
    - Element-wise transformation (function called for each cell)

* transform():
    - Used with groupby to broadcast group-level calculation back to original shape
    - Always returns same shape as input
    - Useful for feature engineering (e.g. normalize by group mean)
"""

# =====================================================
# ================== QUICK RECAP ======================
# =====================================================

"""
📝 Quick Recap – Apply & Transform:

* df.apply(func, axis=0/1) → run func row-wise/column-wise
* series.apply(func) → element-wise on Series
* series.map(func/dict) → fast element-wise transform
* df.applymap(func) → element-wise transform on entire DataFrame
* groupby(...).transform(func) → return group result for each row
* Prefer vectorized operations over apply for speed
"""
