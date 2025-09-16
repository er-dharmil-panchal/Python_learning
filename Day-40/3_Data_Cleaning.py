"""
📌 Pandas – Step 3 (Data Cleaning)

This file covers:
    - Detecting Missing Values (isnull, isna)
    - Filling Missing Values (constant, mean, median, mode)
    - Converting data types safely (errors='coerce')
    - Cleaning strings (strip spaces, fix casing)
    - Handling duplicates (drop_duplicates after cleaning)
    - Replacing values (standardizing categories)
    - Dropping rows with missing values (dropna)
📝 Summary:
    - Always clean data before analysis — missing values, wrong data types, inconsistent text can break results.
    - Use pd.to_numeric(..., errors='coerce') to safely convert columns.
    - Use str.strip(), str.lower(), str.capitalize() for text cleanup.
    - Remove duplicates after cleaning (spaces/case issues can hide duplicates).
"""

import pandas as pd

# =====================================================
# =============== SAMPLE "DIRTY" DATA =================
# =====================================================
data = pd.DataFrame({
    "Name": [" Sagar ", "Dharmil", "Hani", "Sagar ", "Dax", None],
    "Age": ["22", None, "24", "22", "twenty", "21"],
    "City": ["Ahmedabad", "ahmedAbad", "AMD", "Ahmedabad", "Mumbai", " "]
})
print("RAW DATA:")
print(data)

# =====================================================
# =============== DETECT MISSING VALUES ===============
# =====================================================

print("\n👉🏻 Detect Missing Values")
print(data.isnull())                    # True = missing
print(f"Count of null values:\n{data.isnull().sum()}")  # Count per column
print(data.isna())                      # Same as isnull()

# =====================================================
# =============== FILL MISSING VALUES =================
# =====================================================

# 1) Fill with Constant
# data['Name'] = data['Name'].fillna("Unknown")
# print(data['Name'].isnull().sum())    # Now no nulls in 'Name'

# 2) Fill with Mean / Median / Mode (for numeric columns)

# 🔑 Convert Age to numeric safely
# errors='coerce': If value cannot be converted (like "twenty"), replace with NaN instead of error.
# errors='raise' (default): will throw error on bad data.
# errors='ignore': leaves invalid values as-is, no conversion done.

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
print("\nAfter converting 'Age' to numeric (invalid → NaN):")
print(data)

# Fill missing Age with median (you can also use mean or mode)
data['Age'] = data['Age'].fillna(data['Age'].median())

# Preserve integer dtype (nullable Int64 to allow NaN support)
data['Age'] = data['Age'].astype('Int64')
print("\nAfter filling missing Age with median:")
print(data)

# Fill missing City with Mode (most frequent value)
city_mode = data["City"].mode()[0]
data.fillna({"City": city_mode}, inplace=True)
print("\nAfter filling missing City with mode:")
print(data)

# =====================================================
# =========== REMOVE DUPLICATES (Before) ==============
# =====================================================

print("\n👉🏻 Remove Duplicates (Before Cleaning):")
print(data.drop_duplicates())  # Won't work properly yet because of spaces / case diff

# =====================================================
# =============== CLEANING STRING DATA ================
# =====================================================

# Trim extra spaces from Names
data['Name'] = data['Name'].str.strip()

# Standardize City Names
data['City'] = data['City'].str.capitalize()

# Replace alternate spellings manually
data['City'] = data['City'].replace({
    "ahmedabad": "Ahmedabad",  # lowercase fix
    "Amd": "Ahmedabad",        # short form fix
    " ": "Unknown"             # empty space → Unknown
})

print("\nAfter cleaning strings & replacing values:")
print(data)

# =====================================================
# =============== REMOVE DUPLICATES (AFTER) ===========
# =====================================================

data = data.drop_duplicates()
print("\nAfter cleaning & removing duplicates:")
print(data)

# =====================================================
# =============== DROPPING MISSING VALUES =============
# =====================================================

print("\n👉🏻 Dropping Rows with Missing Values")
dirty2 = pd.DataFrame({
    "Name": [" Sagar ", "Dharmil", "Hani", "Sagar ", "Dax", None],
    "Age": ["22", None, "24", "22", "twenty", "21"],
    "City": ["Ahmedabad", "ahmedAbad", "AMD", None, "Mumbai", " "]
})

print("\nOriginal data with missing City:")
print(dirty2)

# Drop rows with missing Age
data1 = dirty2.dropna(axis=0, subset=['Age'], inplace=False)
print("\nAfter dropping rows with missing Age:")
print(data1)

# Fill missing City with default value "Amd"
dirty2.fillna({"City": "Amd"}, inplace=True)
print("\nAfter filling missing City with 'Amd':")
print(dirty2)

"""
📝 Quick Recap:
- Use isnull() / isna() to find missing values
- fillna() → fill missing with constant, mean, median, or mode
- pd.to_numeric(..., errors='coerce') → safely convert numbers
- Clean text with .str.strip(), .str.lower(), .str.capitalize()
- Replace alternate values with .replace()
- drop_duplicates() after cleaning removes true duplicates
- dropna() removes rows with missing data
"""
