"""
📌 OS module
    - it is built-in module of Python
    - provides functions for interacting with the operating system
    - you can perform existing folder operations by automation (create, delete)
    - os is mainly for directories; it will not create .py, .txt files
"""

import os
import shutil

# ----------------------------------------------------
# Create main directory
# ----------------------------------------------------
shutil.rmtree("Folders")  # For avoiding duplicate folder
if not os.path.exists("Folders"):
    os.mkdir("Folders")  # Folder created successfully
    # If run again, it gives error because folder already exists, so we added checking condition

# ----------------------------------------------------
# Create multiple folders (Day-1 to Day-100)
# ----------------------------------------------------
for i in range(1, 101):
    os.mkdir(f"Folders/Day-{i}")
    os.mkdir(f"Folders/Day-{i}/Main.py")  # NOTE: creates folder named Main.py, not a file

    # Rename the folder for Day-10
    if i == 10:
        os.rename(f"Folders/Day-{i}", f"Folders/DAYYYYY-{i}")

    # To remove folders:
    # os.rmdir(f"Folders/Day-{i}")  # For empty folders
    # shutil.rmtree(f"Folders/Day-{i}")  # For non-empty folders

# ----------------------------------------------------
# List folders and their contents
# ----------------------------------------------------
folders = os.listdir("Folders")
for f in folders:
    print(os.listdir(f"Folders/{f}"))

# ----------------------------------------------------
# Basic directory operations
# ----------------------------------------------------
os.system('date')

# Get current directory
print(os.getcwd())  # /Users/dharmilpanchal/Documents/Python

# Change the current working directory
print(os.chdir("Phase-2"))
print(os.getcwd())  # /Users/dharmilpanchal/Documents/Python/Phase-2

# Navigate to Pictures
os.chdir("/Users/dharmilpanchal/Pictures")
print(os.getcwd())  # /Users/dharmilpanchal/Pictures

# Navigate back to Python
os.chdir("/Users/dharmilpanchal/Documents/Python")
print(os.getcwd())  # /Users/dharmilpanchal/Documents/Python

# List contents of current directory
print(os.listdir(path='.'))

# ----------------------------------------------------
# Nested directory operations
# ----------------------------------------------------
os.makedirs("/Users/dharmilpanchal/Documents/Python/Learn/now")
os.removedirs("/Users/dharmilpanchal/Documents/Python/Learn/now")

# ----------------------------------------------------
# File removal (empty files only)
# ----------------------------------------------------
# os.remove("/Users/dharmilpanchal/Documents/Python/Folders/file_to_delete")

# ----------------------------------------------------
# Get file/folder stats
# ----------------------------------------------------
print(os.stat("/Users/dharmilpanchal/Pictures"))

# NOTE:
# This is a very big module to cover, so we can use its functionality when needed and learn over time.

# ----------------------------------------------------
# Path operations (reference)
# ----------------------------------------------------
"""
| Function                 | Description                      | Example                                             |
| ------------------------ | -------------------------------- | --------------------------------------------------- |
| `os.path.exists(path)`   | Check if **file/folder exists**  | `os.path.exists('data.txt')`                        |
| `os.path.isfile(path)`   | Check if path is a **file**      | `os.path.isfile('data.txt')`                        |
| `os.path.isdir(path)`    | Check if path is a **directory** | `os.path.isdir('folder')`                           |
| `os.path.join(a, b)`     | Join paths safely                | `os.path.join('folder', 'file.txt')`                |
| `os.path.abspath(path)`  | Get **absolute path**            | `os.path.abspath('file.txt')`                       |
| `os.path.basename(path)` | Get **file name**                | `os.path.basename('/home/user/file.txt')`           |
| `os.path.dirname(path)`  | Get **directory name**           | `os.path.dirname('/home/user/file.txt')`            |
| `os.path.splitext(path)` | Split **name and extension**     | `os.path.splitext('file.txt')` → `('file', '.txt')` |
"""

# ----------------------------------------------------
# Misc system info
# ----------------------------------------------------
print(os.system("ls"))
print(os.name)
