// basic set inreoduction.
'''
📌 Set in Python
- Sets are unordered collections of unique data items.
- Items are separated by commas and enclosed within curly brackets {}.
- Duplicate values are automatically removed.
Example: a = {1, 2, 2, 3}  →  {1, 2, 3}
'''

# ----------------------------
# 1️⃣ Creating Sets
# ----------------------------
a = {1, 2, 3, 4, 1, 2, 3, 4}
print(a)               # Output may be {1, 2, 3, 4} OR in any other order
print(type(a))         # <class 'set'>

# NOTE: Sets are mutable (you can add/remove items), 
# but their elements themselves must be immutable (like int, str, tuple).
# You cannot change individual elements by index.

# a[0] = 1  # ❌ TypeError: 'set' object does not support item assignment

# ----------------------------
# 2️⃣ No Indexing (Unordered)
# ----------------------------
names = {"Dharmil", "Nihar", "Sakshi", 1, False}
print(names)           # Order may vary
# print(names[0])      # ❌ TypeError: 'set' object is not subscriptable

# ----------------------------
# 3️⃣ Empty Set
# ----------------------------
b = {}                 # This creates an empty dictionary, not a set
print(type(b))         # <class 'dict'>

b = set()              # ✅ Correct way to create empty set
print(type(b))         # <class 'set'>

# ----------------------------
# 4️⃣ Looping through a set
# ----------------------------
for item in names:
    print(item)

# ----------------------------
# 5️⃣ Set Methods
# ----------------------------
s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 6}

# 👉 union(): Returns a new set containing all unique items from both sets
print(s1.union(s2))    # {1, 2, 3, 4, 5, 6}

# 👉 update(): Adds items from another set into the current set
print(s1.update(s2))   # Output: None (because it modifies in place)
print(s1)              # {1, 2, 3, 4, 5, 6}

# 👉 intersection(): Returns a new set with only the common items
print("s1 =", s1, "\ns2 =", s2)
print(s1.intersection(s2))  # {1, 2}
print(s1)                   # s1 is unchanged

# 👉 intersection_update(): Keeps only common items in the set (modifies in place)
print(s1.intersection_update(s2))  # Output: None
print(s1)                          # {1, 2}
