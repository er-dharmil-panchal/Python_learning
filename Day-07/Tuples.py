'''
📌 Tuples in Python
Tuples are same as lists but you cannot change them (immutable).
They store multiple items in a single variable. 
Tuple items are separated by commas and enclosed within round brackets ().
Lists use square brackets [].
"Tuples are immutable, meaning we cannot change them after creation." ✅
'''

import time

# ----------------------------
# 1️⃣ Creating Tuples
# ----------------------------
tuple0 = ("Rahul", 18, "mahesh", 63)
tuple1 = (1, 2, 2, 3, 5, 6)
tuple2 = ("Red", "Green", "Blue")

# Special case: Single element tuple
tuple3 = (1)     # ❌ This is int
tuple31 = (1,)   # ✅ This is tuple

print(tuple0)
print(tuple1)
print(tuple2)

print(type(tuple1))   # tuple
print(type(tuple3))   # int
print(type(tuple31))  # tuple

# NOTE: For a single value tuple, you must add a comma after the value.

# ----------------------------
# 2️⃣ Immutability Example
# ----------------------------
a = (71, 42, 33, 14, 95, 56)
# a[2] = 26  # ❌ TypeError: 'tuple' object does not support item assignment

# List (mutable) example
a1 = [71, 42, 33, 14, 95, 56]
a1[2] = 26   # ✅ Works fine
print(a1, "\n\n")

'''
💡 Why use tuples?
In complex programs, sometimes you have values that should never change
(e.g., coordinates, fixed colors, constants).
'''

# Example: Fixed data
city_location = (19.0760, 72.8777)  # Mumbai coordinates
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# ----------------------------
# 3️⃣ Indexing
# ----------------------------
tuple4 = ("Rahul", 18, 9.9, True)

# Type of each item
print(type(tuple4[0]))
print(type(tuple4[1]))
print(type(tuple4[2]))
print(type(tuple4[3]), "\n\n")

# Positive indexing
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3], "\n\n")

# Negative indexing
print(tuple4[-1])
print(tuple4[-2])
print(tuple4[-3])
print(tuple4[-4], "\n\n")

# ----------------------------
# 4️⃣ Membership Test ('in')
# ----------------------------
tup = (22, 33, 44, 55, 66, 77)

print("yes" if 17 in tup else "no")
print("yes" if 66 in tup else "no")

country = ("Brazil", "Russia", "India", "China", "South Africa")
print("Russia is present." if "Russia" in country else "Russia is absent.")

# ----------------------------
# 5️⃣ Slicing
# ----------------------------
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")

# Positive index slicing
print(animals[3:7])
# Negative index slicing
print(animals[-7:-2])

# Start/end omitted
print(animals[4:])
print(animals[-4:])
print(animals[:6])
print(animals[:-3])

# Step values
print(animals[0:9:2])  # Every 2nd element
print(animals[0:9:3])  # Every 3rd element

# Creating new tuple from old one
tup2 = animals[0:4]
print(tup2)

# ----------------------------
# 6️⃣ Tuple Unpacking
# ----------------------------
person = ("Rahul", 18, "India")
name, age, country = person
print(name, age, country)

# ----------------------------
# 7️⃣ Nested Tuples
# ----------------------------
nested = ((1, 2), (3, 4))
print(nested[0][1])  # Output: 2

# ----------------------------
# 8️⃣ Tuples vs Lists - Performance
# ----------------------------
l = list(range(1_000_000))
t = tuple(range(1_000_000))

start = time.time()
999999 in l
print("List search:", time.time() - start)

start = time.time()
999999 in t
print("Tuple search:", time.time() - start)

# ⚠️ Difference will be small, but tuples often win when:
# - Data is fixed and won’t change
# - Many repeated lookups

'''
📌 NOTE:
- Tuples and strings are immutable
- Lists are mutable
'''
