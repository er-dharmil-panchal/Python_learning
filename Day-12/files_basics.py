"""
📌 Python File Handling

Python allows us to perform operations on files using the built-in `open()` function.

The `open()` function syntax:
    open(filename, mode)

Arguments:
1. filename : Name (and path) of the file
2. mode     : Mode in which the file is opened

Common Modes:
- 'r' : Read → Opens file for reading. Error if file does not exist. Default mode.
- 'w' : Write → Opens file for writing. Creates a new file if it doesn't exist.
- 'a' : Append → Opens file to add content at the end. Creates file if it doesn't exist.
- 'x' : Create → Creates a new file. Error if file already exists.

Text Mode:
- 't' : Text mode. Default mode. Can be combined like 'rt', 'wt', 'at'.
- Example: 'r', 'rt', 'w', 'wt', etc.
"""

# ---------------------------
# Reading a file
# ---------------------------
# Open file in read mode
f = open('file_io/sample.txt', 'r')

# f is a TextIOWrapper object
print(f)              # <_io.TextIOWrapper name='file_io/sample.txt' mode='r' encoding='UTF-8'>
print(type(f))        # <class '_io.TextIOWrapper'>

# Read file contents
content = f.read()
print(content)

# Always close the file after operation
f.close()


# ---------------------------
# Writing to a file
# ---------------------------
# Open file in write mode (creates new file if it doesn't exist)
f = open("file_io/sample2.txt", "w")

# Write content to file
f.write("Hello, this is a new file")

# Close the file
f.close()


# ---------------------------
# Notes
# ---------------------------
# 1. Attempting to read in write mode will cause error:
#    f = open("file_io/sample.txt", "w")
#    f.read()  # → io.UnsupportedOperation: not readable

# 2. Both single (' ') and double (" ") quotes are valid for file names and strings.
