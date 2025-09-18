"""
📌 Pandas – Step 5 (GroupBy & Aggregation)

This file covers:
    - What GroupBy means (Split → Apply → Combine)
    - Basic grouping and single-column aggregations (mean, sum, count)
    - Multiple aggregations at once (.agg)
    - Named aggregation for clean column names
    - Grouping by multiple columns
    - Accessing groups & attributes (groups, get_group)
    - Group-wise transform (add derived columns)
    - Group-wise filtering (like SQL HAVING)
    - Top-N per group (idxmax, nlargest)
    - Custom group functions with apply()
    - Group-wise cumulative operations (cumsum, cumcount)
    - Flattening MultiIndex columns after agg
    - Pivot tables (shortcut for grouped summaries)

📝 Summary:
    - GroupBy = Split → Apply → Combine.
    - groupby(...)[col].agg(func) is the most common pattern.
    - .agg() can take list of functions, or dictionary for per-column ops.
    - Named aggregation is recommended for readable output.
    - transform() → return same shape as original DF (useful for adding new cols).
    - filter() → drop entire groups that don't satisfy condition.
    - idxmax()/nlargest() → pick top rows per group.
    - apply() → ultimate flexibility (but slower).
    - Pivot tables are convenient for cross-tab style reports.
"""

import pandas as pd

# =====================================================
# =============== SAMPLE DATA =========================
# =====================================================
df = pd.DataFrame({
    "Name": ["Amit", "Bela", "Chetan", "Deep", "Esha", "Farah", "Gita"],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science", "Math"],
    "Marks": [88, 92, 75, 92, 60, 75, 88],
    "Attempt": [1, 1, 1, 2, 1, 2, 1]
})
print("RAW DATA:")
print(df)

# =====================================================
# ============ BASIC GROUPING & AGGREGATION ============
# =====================================================

# 👉🏻 1) Average marks per subject
print("\n👉🏻 Average marks per subject")
print(df.groupby("Subject")[["Marks"]].mean())  # DataFrame result

# 👉🏻 2) Count of students per subject
print("\n👉🏻 Count of students per subject")
print(df.groupby("Subject")[["Name"]].count())

# 👉🏻 3) Same using .size() (counts all rows including NaNs)
print("\n👉🏻 Using .size()")
print(df.groupby("Subject").size())

# 👉🏻 4) Explicit aggregation with .agg()
print("\n👉🏻 Count of students per subject with agg()")
print(df.groupby("Subject")[["Name"]].agg("count"))

# =====================================================
# =============== MULTIPLE AGGREGATIONS ===============
# =====================================================

# Multiple functions on one column
print("\n👉🏻 Multiple aggregations on Marks")
print(df.groupby("Subject")["Marks"].agg(["mean", "sum", "count", "max", "min"]))

# 👉🏻 Named aggregation (recommended)
print("\n👉🏻 Named aggregation for clean column names")
result = df.groupby("Subject").agg(
    avg_marks=("Marks", "mean"),
    total_marks=("Marks", "sum"),
    students=("Name", "count")
).reset_index()
print(result)

# 👉🏻 Group by multiple columns
print("\n👉🏻 Group by Subject + Attempt")
print(df.groupby(["Subject", "Attempt"])["Marks"].mean().reset_index())

# =====================================================
# ======= ACCESSING GROUPS & GROUP ATTRIBUTES =========
# =====================================================

g = df.groupby("Subject")
print("\n👉🏻 Groups dictionary:")
print(g.groups)  # keys → list of row indices

print("\n👉🏻 Get group 'Math':")
print(g.get_group("Math"))

# =====================================================
# ========== TRANSFORM → ADD NEW COLUMNS ==============
# =====================================================

# Difference from group mean
df["marks_minus_mean"] = df["Marks"] - df.groupby("Subject")["Marks"].transform("mean")
print("\n👉🏻 Marks - Subject-wise Mean:")
print(df[["Name", "Subject", "Marks", "marks_minus_mean"]])

# =====================================================
# =============== FILTER GROUPS (HAVING) ==============
# =====================================================

print("\n👉🏻 Keep groups with mean Marks >= 80")
print(df.groupby("Subject").filter(lambda g: g["Marks"].mean() >= 80))

# =====================================================
# =============== TOP-N PER GROUP =====================
# =====================================================

# 1) Fast: idxmax() → pick one row per group
print("\n👉🏻 Highest scorer per subject (idxmax)")
idx = df.groupby("Subject")["Marks"].idxmax()
print(df.loc[idx].reset_index(drop=True))

# 2) nlargest() with apply → top 2 per group
print("\n👉🏻 Top-2 students per subject")
top2 = df.groupby("Subject", group_keys=False).apply(lambda g: g.nlargest(2, "Marks")).reset_index(drop=True)
print(top2)

# =====================================================
# =============== APPLY (CUSTOM FUNC) =================
# =====================================================

print("\n👉🏻 Custom summary per group using apply()")
def summary(g):
    return pd.Series({
        "mean": g["Marks"].mean(),
        "count": g["Marks"].count(),
        "range": g["Marks"].max() - g["Marks"].min()
    })

print(df.groupby("Subject").apply(summary).reset_index())

# =====================================================
# ======= GROUP-WISE CUMULATIVE OPERATIONS ============
# =====================================================

print("\n👉🏻 Group-wise cumulative sum of Marks")
df["cum_marks_in_group"] = df.groupby("Subject")["Marks"].cumsum()
print(df[["Name", "Subject", "Marks", "cum_marks_in_group"]])

# =====================================================
# ===== MULTIINDEX COLUMNS & PIVOT TABLE ==============
# =====================================================

multi = df.groupby("Subject").agg({"Marks": ["mean", "sum"], "Attempt": ["max"]})
print("\n👉🏻 MultiIndex columns after agg:")
print(multi)

print("\n👉🏻 Flatten MultiIndex columns:")
multi.columns = ["_".join(col) for col in multi.columns]
print(multi.reset_index())

# 👉🏻 Pivot Table (shortcut)
print("\n👉🏻 Pivot Table - Average Marks per Subject x Attempt")
print(pd.pivot_table(df, index="Subject", columns="Attempt", values="Marks", aggfunc="mean"))
