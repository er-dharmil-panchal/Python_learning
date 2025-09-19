"""
📌 Pandas – Step 6 (Joining & Merging)
    - This is just like SQL joins or Excel’s VLOOKUP.
    - Real-world data is often split across tables:
        - students → master data
        - scores → transactions / events
            To answer “What marks did each student get?” we must merge on id.

    This file covers:
    - Merging DataFrames (like SQL joins or Excel VLOOKUP)
    - Inner, Left, Right, Outer joins
    - Merging on different column names
    - Merging on multiple keys (composite key)
    - Handling overlapping column names with suffixes
    - Concatenation (vertical and horizontal stacking)
    - join() shortcut (index-based joins)
    - combine_first() → fill missing values from another DataFrame
    - Debugging merges (indicator=True)

📝 Summary:
    - merge() → column-based joins
    - join() → index-based joins (shortcut)
    - combine_first() → fill NaNs from another DataFrame
    - suffixes → resolve overlapping column names
    - multi-key merge → combine multiple columns as composite keys
"""
import pandas as pd

# =====================================================
# =============== SAMPLE DATA =========================
# =====================================================

students = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Amit", "Bela", "Chetan", "Deep"],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"]
})

scores = pd.DataFrame({
    "id": [1, 2, 2, 5],
    "subject": ["Math", "Math", "Science", "Math"],
    "marks": [88, 92, 85, 60]
})

print("\n👉🏻 Student data")
print(students)
print("\n👉🏻 Scores data")
print(scores)

# =====================================================
# ============= INNER JOIN (default) ==================
# =====================================================

print("\n👉🏻 Default inner join with 'id'")
inner_join = pd.merge(students, scores, on="id")  # only rows with matching id in both
print(inner_join)
# Deep (id=4) is missing → no score
# id=5 (from scores) is missing → no student info

# =====================================================
# =============== DIFFERENT JOIN TYPES ================
# =====================================================

# 1) Left join → keep all rows from left DataFrame
print("\n👉🏻 Left join with 'id'")
left_join = pd.merge(students, scores, on="id", how="left")
print(left_join)
# Missing scores → NaN

# 2) Right join → keep all rows from right DataFrame
print("\n👉🏻 Right join with 'id'")
right_join = pd.merge(students, scores, on='id', how='right')
print(right_join)
# Missing student info → NaN

# 3) Outer join → union of keys
print("\n👉🏻 Outer join with 'id'")
outer_join = pd.merge(students, scores, on='id', how='outer')
print(outer_join)
# All rows from both DataFrames, NaN where missing

# =====================================================
# ========= Merging on Different Column Names =========
# =====================================================

# When two DataFrames have the same logical key but the column names differ, you can’t just do on='column'.
# Instead, Pandas provides:
#   left_on → column in the left DataFrame
#   right_on → column in the right DataFrame
students11 = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Amit", "Bela", "Chetan"],
    "city": ["Delhi", "Mumbai", "Delhi"]
})

print("\n👉🏻 with different column name , inner join with 'student_id' and 'id'")
print(pd.merge(students11, scores, left_on="student_id", right_on="id", how="inner"))
# print(pd.merge(students11,scores,on="id",how="left"))

## can be done with index

# Left DataFrame: students (index = student ID)
students12 = pd.DataFrame({
    "name": ["Amit", "Bela", "Chetan"],
    "city": ["Delhi", "Mumbai", "Delhi"]
}, index=[1, 2, 3])  # student IDs as index

# Right DataFrame: scores (index = student ID)
scores12 = pd.DataFrame({
    "subject": ["Math", "Science", "Math"],
    "marks": [88, 92, 60]
}, index=[1, 2, 4])  # note: id=4 has no student

print("\n👉🏻 with index")
print(pd.merge(students, scores, left_index=True, right_index=True, how="inner"))

# =====================================================
# ============= Merging on Multiple Keys ==============
# =====================================================

# Left DataFrame: students + exam attempt
students12 = pd.DataFrame({
    "id": [1, 2, 2, 3],
    "exam": [1, 1, 2, 1],
    "name": ["Amit", "Bela", "Bela", "Chetan"]
})

# Right DataFrame: scores per student per attempt
scores12 = pd.DataFrame({
    "student_id": [1, 2, 2, 2, 4],
    "exam_num": [1, 1, 2, 3, 1],
    "subject": ["Math", "Math", "Science", "Math", "Math"],
    "marks": [88, 92, 85, 70, 60]
})

print("\n👉🏻 Merging on Multiple Keys")
print(pd.merge(students12, scores12, left_on=['exam', 'id'], right_on=['exam_num', 'student_id'], how="inner"))

# Handling Overlapping Column Names
print("\n👉🏻Handling Overlapping Column Names")
left = pd.DataFrame({
    'id': [1, 2],
    'city': ['Delhi', 'Mumbai'],
    'name': ['Amit', 'Bela']
})

right = pd.DataFrame({
    'id': [1, 2],
    'city': ['Delhi', 'Pune'],
    'marks': [88, 92]
})

# Merge without specifying suffixes
# Only applies to overlapping columns that are not keys
# NOTE -> if column names are different, suffixes does nothing — Pandas keeps the original names
merge_default = pd.merge(left, right, on='id')
print("Default suffixes (_x,_y):")
print(merge_default)
merge_custom = pd.merge(left, right, on='id', suffixes=('_student', '_exam'))
print("\nCustom suffixes:")
print(merge_custom)

## Merging on Multiple Keys
# Sometimes a single column is not enough to uniquely identify rows.
# Pandas allows you to merge on multiple columns (composite key) using:
students12 = pd.DataFrame({
    "id": [1, 2, 2, 3],
    "exam": [1, 1, 2, 1],
    "name": ["Amit", "Bela", "Bela", "Chetan"],
    "city": ["Delhi", "Mumbai", "Mumbai", "Delhi"]
})

# Right DataFrame: exam scores per student per attempt
scores12 = pd.DataFrame({
    "student_id": [1, 2, 2, 2, 4],
    "exam_num": [1, 1, 2, 3, 1],
    "subject": ["Math", "Math", "Science", "Math", "Math"],
    "marks": [88, 92, 85, 70, 60],
    "exam_city": ["Delhi", "Pune", "Mumbai", "Chennai", "Mumbai"]
})

merged_multi = pd.merge(students12, scores12, left_on=['id', 'exam'], right_on=['student_id', 'exam_num'], how="inner")
print("\n👉🏻 Merged on Multiple Keys (inner join):")
print(merged_multi)

# If students['id'] is int64 but scores['student_id'] is str, merge will fail. Use .astype(int) or .astype(str) to fix.
# Suffixes: Only used when there are overlapping non-key columns.

# Pandas keeps all columns from both DataFrames
print("### cleen data with drop the same columns")
print(merged_multi.drop(columns=['student_id', 'exam_num']))

# =====================================================
# ======== Concatenation (Stacking DataFrames) ========
# =====================================================

# 👉🏻 Vertical (like SQL UNION)
print("\n👉🏻 Vertical (like SQL UNION)")
print(pd.concat([students12, scores12]))
# 👉🏻 Horizontal (side-by-side)
print("\n👉🏻 Horizontal (side-by-side)")
print(pd.concat([students12, scores12], axis=1, join='inner'))
# 👉🏻 Keys — MultiIndex for Source Identification
print("\n👉🏻 Keys — MultiIndex for Source Identification")
print(pd.concat([students12, scores12], axis=0, join='outer', keys=["student12", "score12"]))

# Quick Note:
# axis=0 -> vertical, axis=1 -> horizontal
# ignore_index=True → resets index, useful for stacked DataFrames
# Different columns → outer join fills missing with NaN, inner join keeps only common columns
# Keys -> hierarchical index to track origin of rows
# Concatenation does not merge on any key - it simply stacks

# =====================================================
# =========== join() Shortcut (Index-based) ===========
# =====================================================

print("\n👉🏻 Join shortcut (Index-based)")
print("If scores is indexed by id ")
scores_indexed = scores.set_index('id')
print(students.join(scores_indexed, on='id', how="inner"))
print(f"\n👉🏻Direct join \n{students.join(scores, how="inner", lsuffix="_students", rsuffix="_score")}")

df1 = pd.DataFrame({
    "name": ["Amit", "Bela", "Chetan"],
    "city": ["Delhi", "Mumbai", "Delhi"]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "marks": [88, 92, 75],
    "subject": ["Math", "Science", "Math"]
}, index=[1, 2, 3])

# Join using index (default: left join)
print("\n👉🏻 Join using index (default left join)")
print(df1.join(df2))

# Quick Note:
# Default join is left (keeps left index, adds matching right columns).
# join() is index-based — use merge() for column-based keys.
# lsuffix/rsuffix → only needed when columns overlap.
# Can join multiple DataFrames by passing a list.
# how='outer' → include all indexes, how='inner' → only indexes present in all DataFrames.


# =====================================================
# ================== combine_first() ==================
# =====================================================

# Fill Missing from Another DF
# Takes values from a unless missing -> then fill from b.

# Primary DataFrame
df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Amit", None, "Chetan"],
    "marks": [88, 92, None]
}).set_index("id")

# Secondary DataFrame (backup)
df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Amit Kumar", "Bela", "Chetan Sharma"],
    "marks": [None, 85, 75],
    "city": ["Delhi", "Mumbai", "Delhi"]
}).set_index("id")

print("\n👉🏻 Combined DataFrame (fill NaNs from df2):")
print(df1.combine_first(df2))

# =====================================================
# ============ DEBUGGING MERGES (indicator) ==========
# =====================================================

print("\n👉🏻 Debugging merges with indicator=True")
print(pd.merge(students, scores, on='id', how='outer', indicator=True))
# Adds _merge column: left_only, right_only, both.

# =====================================================
# ================== QUICK RECAP ======================
# =====================================================

"""
📝 Quick Recap – Joining & Merging:

* merge(df1, df2, on='col') → inner join by default
* left_on / right_on → merge when column names differ
* how='left'/'right'/'outer'/'inner' → control which keys are kept
* suffixes=('x','y') → handle overlapping non-key columns
* merge on multiple keys → composite key using left_on=[...], right_on=[...]
* join() → index-based shortcut (default left join)
* concat() → stack DataFrames vertically (axis=0) or horizontally (axis=1)
* combine_first() → fill NaNs from another DataFrame
* indicator=True → track source of rows (left_only, right_only, both)
"""
