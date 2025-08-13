'''
----------------- LIST IS ONE OF THE MOST IMPORTANT TOPICS -----------------

→ List is a Data Type in Python.
→ A list can store multiple items in a single variable.
   Example: List of marks of 8 students, list of people living in India — 
   you can call them with one name.

- Lists are an ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are mutable (changeable), meaning we can alter them after creation.

NOTE: Lists and tuples are similar, but tuples are immutable (cannot be changed after creation), 
while lists can be modified.
'''

# ---------------------------- Basic List Creation ----------------------------

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nThis is a list:", l)
print("Type of l is:", type(l))

marks = [33, 55, 23]
print(marks)
print(marks[1])

# Example: 3 students' marks in one list
# Rahul (roll number: 0), Mahesh (roll number: 1), Dharmil (roll number: 2)

print("Rahul's Marks =", marks[0])
print("Mahesh's Marks =", marks[1])
print("Dharmil's Marks =", marks[2])
print()

# ---------------------- Heterogeneous List Example ----------------------
# We can store integers, floats, strings, booleans in the same list,
# but it reduces consistency and readability.

mixed_list = [1, 2, 3.4, "Dharmil", True]
print(mixed_list[3])
print(type(mixed_list[1]))  # int
print(type(mixed_list[2]))  # float
print(type(mixed_list[3]))  # str
print(type(mixed_list[4]))  # bool
print(mixed_list)

# Processing heterogeneous list → Use isinstance to avoid errors
total = 0
for i in mixed_list:
    if isinstance(i, (int, float)):
        total += i
print("Total =", total)

'''
Each element in a list has a unique index.
First item has index [0], second item [1], and so on.
'''

# ---------------------------- Negative Index ----------------------------

n = [1, 2, 17, 4, 5]
# Easy way to find negative index:
# n[-3] == len(n) - 3 == n[5 - 3] == n[2]
print(n[-3])

# ---------------------------- Membership Check ----------------------------
if 17 in n:
    print("Yes")
else:
    print("No")

if "Dharmil" in mixed_list:
    print("Yes")
else:
    print("No")

# ---------------------------- Slicing ----------------------------
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)
print(l[:])  # full copy

print(l[5:8])      # starts at index 5, ends at index 7
print(l[1:-1])     # same as l[1:8]

# Jump slicing
print("Jump by 2:", l[0:9:2])
print("Jump by 3:", l[0:9:3])
print("\n")

# ---------------------------- List Comprehension ----------------------------

# Without comprehension
nums = [1, 2, 3, 4]
squares = []
for num in nums:
    squares.append(num * num)
print(squares)  # [1, 4, 9, 16]

# With comprehension
squares = [num * num for num in nums]
print(squares)

# With condition
nums = [1, 2, 3, 4, 5, 6]
even_squares = [n * n for n in nums if n % 2 == 0]
print(even_squares)  # [4, 16, 36]

# More examples
lst = [i for i in range(1, 5)]
print(lst)

lst1 = [i * i for i in range(1, 5)]
print(lst1)

lst2 = [(i + 1) / 2 for i in range(1, 10)]
print(lst2)

lst3 = [i for i in range(1, 10) if i % 2 == 0]
print(lst3)
print("\n")

# ---------------------------- List Methods ----------------------------

lst4 = [1, 2, 3, 4, 5, 6, 7]

# append() → add at the end
lst4.append(0)
lst4.append(47)
print(lst4, "\n")

# sort()
lst5 = [45, 23, 67, 2, 3, 4, 623, 7, 97, 121]
lst5.sort()
print(lst5)

lst5.sort(reverse=True)
print(lst5)

# alphabetical sort
colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors, "\n")

# reverse()
lst7 = [1, 22, 34, 23, 11]
lst7.reverse()
print(lst7, "\n")

# index()
print(lst7.index(22))
print(lst7.index(34))
colors = ["violet", "indigo", "blue", "green"]
print(colors.index("green"), "\n")

# count()
lst8 = [4, 7, 4, 2, 3, 5, 8, 7, 6, 45, 3, 2, 3, 4]
print(lst8.count(4))

# copy()
l = [1, 2, 3, 4, 5]
m = l
m[0] = 0
print(m)
print(l, "\n")

l1 = [1, 2, 3, 4, 5]
m1 = l1.copy()
m1[0] = 15
print(m1)
print(l1, "\n")

# insert()
lst9 = [2, 6, 0, 4, 2]
lst9.insert(3, 13)
lst9.insert(300, 13)  # index beyond length → goes to end
print(lst9)

lst91 = ["Dharmil", "Raj", "Prakash", "Preyash"]
lst91.insert(3, "Maheep")
print(lst91)

# remove()
lst91.remove("Raj")
print(lst91)

# pop()
print(lst91.pop())  # remove last
print(lst91)
lst91.pop(2)
print(lst91)

# clear()
lst91.clear()
print(lst91)  # []

# extend()
lst10 = [111, 222, 333, 444]
lst11 = [555, 666, 777, 111]
lst10.extend(lst11)
print(lst10)

# concatenation (without modifying original)
lst10 = [111, 222, 333, 444]
lst11 = [555, 666, 777, 888]
c = lst10 + lst11
print(c)

# ---------------------------- Nested Lists ----------------------------
matrix = [[1, 2, 3], [4, 5, 6]]
for row in matrix:
    for value in row:
        print(value, end=' ')
    print()

# can also do like this
matrix = [[1, 2], [1, 2, 3, 4]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

# ---------------------------- Enumerate ----------------------------
names = ["A", "B", "C"]
print("----- Enumerate -----")
for i, name in enumerate(names):
    print(i, name)

# ---------------------------- zip() ----------------------------
one = [1, 2, 3]
two = [4, 5, 6]
three = [7, 8, 9, 10]

print("----- zip with 2 lists -----")
for o, t in zip(one, two):
    print(o, t)

print("\n----- zip with 3 lists -----")
for o, t, te in zip(one, two, three):
    print(o, t, te)

# NOTE: 10 will not print, because zip() stops at the shortest iterable



# ---------------------------- List Practice ----------------------------



# -------------------------
# 1. Even / Odd Separation (List Comprehension)
# -------------------------
main = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Odd numbers: (i + 1) % 2 == 0 means i is odd
odd = [i for i in main if (i + 1) % 2 == 0]

# Even numbers: (i + 1) % 2 != 0 means i is even
even = [i for i in main if (i + 1) % 2 != 0]

print("Odd:", odd)
print("Even:", even)


# -------------------------
# 2. Student Scores (zip)
# -------------------------
names = ["Rahul", "Mahesh", "Dharmil"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} = {score}")
print()


# -------------------------
# 3. Matrix Printing (Nested Loops)
# -------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()


# -------------------------
# 4. Merge & Sort Lists
# -------------------------
list1 = [1, 4, 5]
list2 = [2, 3, 6]
merged_sorted = sorted(list1 + list2)
print(merged_sorted)


# -------------------------
# 5. Reverse Words in a String
# -------------------------
# Example: "Python is easy" → "easy is Python"
text = "Python is easy"
result = " ".join(text.split()[::-1])
print(result)


# -------------------------
# 6. Max & Min Values
# -------------------------
print("Max:", max(main))
print("Min:", min(main))


# -------------------------
# 7. Count Occurrences
# -------------------------
lst = [1, 1, 1, 1, 11, 2, 2]
print("Count of 1:", lst.count(1))


# -------------------------
# 8. Remove Duplicates (Important)
# -------------------------
#⚠️ NOTE: Don't modify a list while looping over it directly
# because elements shift and some are skipped.
# Example:
# lst = [1, 2, 2, 3]
# Iteration steps:
#   index=0 → sees 1 → remove 1 → lst becomes [2, 2, 3]
#   index=1 → now points to the second 2 → first 2 is skipped
#         All elements to the right shift left
#         The loop moves to the next index
#         Problem becomes worse if 3+ identical items are next to each other:

# --- Option 1: Make a copy ---
lst = [1, 2, 2, 3]
lst_copy = lst.copy()
for i in lst_copy:
    if lst.count(i) > 1:
        lst.remove(i)
print(lst)

# --- Option 2: Build a new list ---
lst = [1, 2, 2, 3]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)  # Keeps original order

# --- Option 3: Use set (fastest, but order changes) ---
lst = [1, 2, 2, 3]
lst = list(set(lst))
print(lst)
