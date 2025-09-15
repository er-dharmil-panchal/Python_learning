"""
📌 Pandas – Step 2 (Indexing & Selection)

This file covers:
    - Column Selection (Single / Multiple)
    - Row Selection (loc / iloc)
    - Row + Column Selection
    - Row & Column Slicing
    - Boolean Indexing (Filtering)
    - Column Assignment, Creation, Updating, Dropping
📝 Summary:
    - Use [] or [['col1','col2']] to select columns.
    - Use loc[] for label-based row/column access (inclusive slicing).
    - Use iloc[] for position-based row/column access (exclusive slicing).
    - Boolean indexing filters rows based on conditions.
    - You can create, update, or drop columns directly with assignment & drop().
"""

import pandas as pd

# =====================================================
# =============== SAMPLE DATA =========================
# =====================================================
s2 = pd.DataFrame(
    [["Dharmil", 18, "Ahmedabad"],
     ["Hani", 19, "Ahmedabad"],
     ["Dax", 19, "Ahmedabad"]],
    index=[1, 2, 3],
    columns=["Name", "Age", "City"]
)
print(s2)

# =====================================================
# =============== COLUMN SELECTION ====================
# =====================================================

# 👉🏻 Single Column → returns a Series
print(f"Single column value (Name of index 1): {s2['Name'][1]}")
# ⚠️ Remember: Our index starts at 1, so ['Name'][0] will NOT work.

# 👉🏻 Multiple Columns → returns a DataFrame
print(f"\nMultiple columns (Name & Age):\n{s2[['Name', 'Age']]}")

# =====================================================
# =============== ROW SELECTION =======================
# =====================================================

# 👉🏻 Select Row by Label → loc[]
print(f"\nSelecting single row by label using loc[]:\n{s2.loc[2]}\n")

# 👉🏻 Select Multiple Rows → loc[]
print(f"Selecting multiple rows by label using loc[]:\n{s2.loc[[2, 3]]}\n")

# 👉🏻 Select Row by Position → iloc[]
print(f"Selecting first row by position using iloc[]:\n{s2.iloc[0]}\n")
print(f"Selecting first three rows by position using iloc[]:\n{s2.iloc[[0, 1, 2]]}\n")

# =====================================================
# =============== ROW + COLUMN SELECTION ==============
# =====================================================

# 👉🏻 Single Row, Specific Columns
print(f"\nSingle value (Row 1, Column 'Name'): {s2.loc[1, 'Name']}")
print(f"Single row, two columns (Series):\n{s2.loc[1, ['Name', 'Age']]}")
print(f"Single row, two columns (DataFrame):\n{s2.loc[[1], ['Name', 'Age']]}")

# 👉🏻 Multiple Rows + Multiple Columns
print(f"\nMultiple rows + columns using loc[]:\n{s2.loc[[1, 3], ['Name', 'Age']]}")
print(f"Multiple rows + columns using iloc[]:\n{s2.iloc[[0, 2], [0, 1]]}")

# =====================================================
# =============== ROW & COLUMN SLICING ================
# =====================================================

# 👉🏻 Using loc[] → inclusive
print(f"\nSlicing rows using loc[] (inclusive):\n{s2.loc[1:3]}")

# 👉🏻 Using iloc[] → exclusive
print(f"Slicing rows using iloc[] (exclusive of end):\n{s2.iloc[0:3]}")

# =====================================================
# =============== COMMON MISTAKE EXAMPLE ==============
# =====================================================

# ❌ Incorrect way – This only selects a single column ("Age")
print(f"\nIncorrect way: s2[['Name','Age'][1]] → \n{s2[['Name', 'Age'][1]]}")

# ✅ Correct way to get specific row + multiple columns
print(f"\nCorrect way:\n{s2.loc[2, ['Name', 'Age']]}")

# Label vs positional indexing:
print(f"\nUsing label-based indexing (loc):\n{s2.loc[2, ['Name', 'Age']]}")
print(f"\nUsing positional indexing (iloc):\n{s2.iloc[1, :]}")

# =====================================================
# =============== BOOLEAN INDEXING ====================
# =====================================================

print(f"\nBoolean indexing (Age > 18):\n{s2[s2['Age'] > 18]}")

# =====================================================
# =============== COLUMN ASSIGNMENT & CREATION ========
# =====================================================

# Creating a new column with condition
s2['Valid'] = s2['Age'] > 18
print(f"\nDataFrame after adding 'Valid' column:\n{s2}")

# Creating new column using vectorized operations
s2['Code'] = s2['Name'] + s2['City']
print(f"\nDataFrame after adding 'Code' column:\n{s2}")

# Updating existing column
s2['Name'] = s2['Name'] + "P"

# Updating with arithmetic operations
s2['Age'] *= 2

# Dropping a column
s2 = s2.drop(columns="Code")
print(f"\nDataFrame after dropping 'Code' column:\n{s2}")

# =====================================================
# ==================== QUICK RECAP ====================
# =====================================================

"""
📝 Quick Recap:
- Column selection → ['col'] (Series), [['col1','col2']] (DataFrame)
- Row selection → loc[label], iloc[position]
- Row + column selection → loc[row, col] or iloc[row_idx, col_idx]
- Slicing → loc is inclusive, iloc is exclusive
- Boolean indexing → filter rows based on condition
- Column assignment → create/update columns directly (vectorized)
- Drop column → drop(columns='col_name')
"""
