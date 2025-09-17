"""
📌 Pandas – Step 4 (Filtering, Sorting & Ranking)

This file covers:
    - Filtering rows (Boolean indexing, multiple conditions, isin, between, query)
    - Using .loc for filtering + column selection (best practice)
    - String filtering with .str (contains, startswith, endswith)
    - Sorting by values (single/multiple columns, ascending/descending)
    - Sorting by index (row labels)
    - nlargest() / nsmallest() for top-N selection
    - Ranking data (rank students, handle ties with different methods)
    - Combining filtering + sorting for real-world use
📝 Summary:
    - Filtering selects rows using conditions (with .loc preferred over chained indexing).
    - Use .str methods for text filtering (case-sensitive by default).
    - sort_values() arranges rows by one or more columns.
    - nlargest()/nsmallest() is fastest for top/bottom N rows.
    - sort_index() sorts by row labels.
    - rank() assigns position numbers (1st, 2nd...) based on a column.
    - Combine filter → sort → head() to get top results easily.
"""

import pandas as pd

# =====================================================
# =============== SAMPLE DATA =========================
# =====================================================
df = pd.DataFrame({
    "Name": ["Amit", "Bela", "Chetan", "Deep", "Esha", "Farah"],
    "Marks": [88, 92, 75, 92, 60, 75],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
})
print("RAW DATA:")
print(df)

# =====================================================
# =================== FILTERING =======================
# =====================================================

# 👉🏻 1) Boolean Filtering
print("\n👉🏻 Filter rows where Marks > 70:")
print(df[df["Marks"] > 70])

# 👉🏻 2) Multiple Conditions (AND / OR)
print("\n👉🏻 Filter rows where Marks > 70 AND Subject = 'Math':")
print(df[(df["Marks"] > 70) & (df["Subject"] == "Math")])

print("\n👉🏻 Filter rows where Marks < 70 OR Subject = 'Science':")
print(df[(df["Marks"] < 70) | (df["Subject"] == "Science")])

# 👉🏻 3) isin() → filter if value is in a list
print("\n👉🏻 Filter where Subject is either Math or Science (ALL here):")
print(df[df["Subject"].isin(["Math", "Science"])])

# 👉🏻 4) between() → range filtering
print("\n👉🏻 Filter rows where Marks are between 70 and 90:")
print(df[df["Marks"].between(70, 90)])

# 👉🏻 5) query() → SQL-like syntax (easy to read)
print("\n👉🏻 Using query() method:")
print(df.query("Marks > 70 and Subject == 'Science'"))
x = 60
print("With threshold value \n",df.query("Marks == @x"))

# 👉🏻 6) Use .loc to filter and select columns (preferred)
print(df.loc[df['Marks'] < 80, ['Name', 'Marks']])

# 👉🏻 7) String filters via .str
# Filter names containing "am" (case-insensitive): can control case sensitive with True and False, by default is True
print("Name contains 'am' \n",df[df['Name'].str.contains('am', case=False)])
# Startswith / endswith:  case-sensitive
print(f"Name that starts with 'A' {df[df['Name'].str.startswith('A')]}")
print(f"Name that ends with 'a' {df[df['Name'].str.endswith('a')]}")


# Avoid chained indexing
# Bad
print(df[df['Marks'] > 70]['Name'])  # works but can cause warnings when assigning later
# Better
print(df.loc[df['Marks'] > 70, 'Name'])


# =====================================================
# =============== SORTING BY VALUES ===================
# =====================================================

# 👉🏻 Sort by one column
print("\n👉🏻 Sort by Marks (Ascending):")
print(df.sort_values(by="Marks"))

# 👉🏻 Sort by one column (Descending)
print("\n👉🏻 Sort by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))

# 👉🏻 Sort by multiple columns
print("\n👉🏻 Sort by Marks (Descending), then Name (Ascending):")
print(df.sort_values(by=["Marks", "Name"], ascending=[False, True]))

# 👉🏻 Reset index after sorting (optional but common)
print("\n👉🏻 Sort by Marks and reset index:")
print(df.sort_values(by="Marks", ascending=False).reset_index(drop=True))

# 👉🏻 Sort by index (row labels)
print(df.sort_index() )          # ascending by index
print(df.sort_index(ascending=False))

# 👉🏻 nlargest() / nsmallest() — fast top-N for numeric columns
print("Top 3 largest \n",df.nlargest(3, 'Marks'))   # top 3 by Marks
print("Last 2 (Smallest) \n",df.nsmallest(2, 'Marks'))  # bottom 2 by Marks



#NOTE:- inplace=True works but pandas sometimes discourages it — explicit assignment is clearer.


# =====================================================
# =============== SORTING BY INDEX ====================
# =====================================================

print("\n👉🏻 Sort by Index (Row Labels):")
print(df.sort_index(ascending=False))

# =====================================================
# =============== RANKING DATA ========================
# =====================================================

# 👉🏻 Rank students based on Marks
print("\n👉🏻 Ranking Students by Marks (Highest = Rank 1):")
df["Rank"] = df["Marks"].rank(ascending=False)
print(df)

# 👉🏻 Different ranking methods
print("\n👉🏻 Ranking with Different Methods (when there are ties):")
print("Average (default): Gives mean of tied positions\n", df["Marks"].rank(method="average", ascending=False))
print("Min: Gives lowest rank to all ties\n", df["Marks"].rank(method="min", ascending=False))
print("Max: Gives highest rank to all ties\n", df["Marks"].rank(method="max", ascending=False))
print("Dense: Like 'min' but without gaps in ranks\n", df["Marks"].rank(method="dense", ascending=False))

# =====================================================
# =============== COMBINE FILTER + SORT ===============
# =====================================================

print("\n👉🏻 Real-World Example: Get Top 3 Students with Marks > 70:")
top3 = df[df["Marks"] > 70].sort_values(by="Marks", ascending=False).head(3)
print(top3)

# =====================================================
# ==================== QUICK RECAP ====================
# =====================================================

"""
📝 Quick Recap:
- Filter rows → df[df['col'] > value] or use df.loc[condition, ['cols']]
- Combine conditions with & (AND) and | (OR)
- isin() → filter rows matching a list
- between() → filter for a range
- query("condition") → SQL-like filtering
- String filters → .str.contains(), .str.startswith(), .str.endswith()
- Avoid chained indexing → use .loc for safe selection + assignment

- sort_values(by='col') → sort by one column
- sort_values(by=['col1','col2'], ascending=[True,False]) → multiple sort
- nlargest()/nsmallest() → fastest top-N/bottom-N selection
- reset_index(drop=True) → get clean index after sorting
- sort_index() → sort by row labels

- rank() → assign ranks based on a column
  • method='average' (default): average of tied ranks
  • method='min': lowest rank to all ties
  • method='max': highest rank to all ties
  • method='dense': like min but no gaps in ranks

- Combine steps: filter → sort → head() → perfect for top-N analysis
"""
