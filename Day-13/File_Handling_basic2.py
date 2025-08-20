# =========================================================
# File Handling in Python
# =========================================================

# ----------------------------
# 1. Read Mode ('r')
# ----------------------------
# Opens file for reading (default mode).
f = open("file_io/sample.txt", 'r')
print(f.read())             # Reads whole file
f.close()

# ----------------------------
# 2. Write Mode ('w')
# ----------------------------
# Creates new file if not exist, else overwrites content.
f2 = open("file_io/sample.txt", 'w')
print(f2.write("helloooo"))   # ans = 8 (number of chars written)
f2.close()

# After this, old content is replaced!

# ----------------------------
# 3. Append Mode ('a')
# ----------------------------
# Appends content to end of file (doesn't replace).
f3 = open("file_io/sample.txt", 'a')
print(f3.write(" after hello "))  # ans = 13
f3.close()
# sample.txt -> "helloooo after hello"

# ----------------------------
# 4. Create Mode ('x')
# ----------------------------
# Creates a new file, raises error if file already exists.
# f4 = open("file_io/sample3.txt", 'x')
# FileExistsError if run again

# ----------------------------
# 5. Text Mode ('t') & Binary Mode ('b')
# ----------------------------
# 't' = text files (default), 'b' = binary (images, videos, pdf etc.)

# Example: Reading in binary
f1 = open("file_io/sample2.txt", "rb")
print(f1.read())             # ans = b'Hello this is new file 1'
f1.close()

# ----------------------------
# 6. Case Sensitivity
# ----------------------------
# 'w' works but 'W' doesn’t (all modes are lowercase).

# ----------------------------
# 7. close() vs with statement
# ----------------------------
# Always close file after work. Better: use 'with' (auto closes).

# Normal way
f1 = open("file_io/sample3.txt", 'w')
f1.write("Python")
f1.close()

# Using 'with' (auto close)
with open("file_io/sample3.txt", 'w') as f:
    f.write("this is using with")
