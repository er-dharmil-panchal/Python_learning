"""
📌 Dictionaries in Python
- Ordered collection of key-value pairs, fast access by key.
"""

# -----------------------------
# 1. Creating a dictionary
# -----------------------------
a = {1: "Dharmil", 2: "Nihar"}  # Define a dictionary
print(type(a))      # <class 'dict'>
print(a)            # {1: 'Dharmil', 2: 'Nihar'}

# -----------------------------
# 2. Accessing single values
# -----------------------------
a = {"Python": ".py", 1: "Python"}

print(a.get("Python"))      # Access using get()
print(a["Python"])          # Access using []

print(a.get("abcdxyz"))     # Returns None if key not found
# print(a["abcdxyz"])       # KeyError if key not found

# -----------------------------
# 3. Accessing multiple values
# -----------------------------
print(a.values())           # Get all values

# -----------------------------
# 4. Accessing keys
# -----------------------------
print(a.keys())             # Get all keys

# -----------------------------
# 5. Accessing key-value pairs
# -----------------------------
for key in a.keys():        # Loop through keys
    print(f"The value corresponding to the key {key} is {a[key]}")

for key, value in a.items():  # Loop with unpacking
    print(f"The value corresponding to the key {key} is {value}")

# -----------------------------
# 6. Updating / Adding items
# -----------------------------
a.update({"Dharmil": 13})  # Update or add key-value
a.update({"Dharmil": 26})
b = {"India": 3}
a.update(b)

a["Java"] = ".java"        # Add new key-value
a[1] = "Python 3"          # Update existing key
print(a)

# -----------------------------
# 7. Removing items
# -----------------------------
b.clear()                   # Remove all items
print(b)

print(a.pop("Java"))        # Remove by key
print(a)

print(a.popitem())          # Remove last inserted item
del a["Dharmil"]            # Delete specific key
print(a)

del a                       # Delete dictionary entirely
# print(a)   # NameError

# -----------------------------
# 8. Checking if a key exists
# -----------------------------
a = {"Python": ".py", 1: "Python"}
print("Python" in a)        # Check key existence
print("Java" in a)

# -----------------------------
# 9. Nested dictionaries
# -----------------------------
students = {
    "Dharmil": {"age": 22, "course": "CS"},
    "Nihar": {"age": 21, "course": "IT"}
}
print(students["Dharmil"]["age"])  # Access nested value

# -----------------------------
# 10. Copying a dictionary
# -----------------------------
a_copy = a.copy()           # Shallow copy
print(a_copy)

# -----------------------------
# 11. Merging dictionaries (Python 3.9+)
# -----------------------------
c = {"C++": ".cpp"}
merged = a | c              # Merge dictionaries
print(merged)

# -----------------------------
# 12. setdefault() method
# -----------------------------
a.setdefault("JavaScript", ".js")  # Get or add key with default
print(a)
