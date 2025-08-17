# 📈 Python Learning Progress Log

---

## 🗓️ Day 0 – Setup (August 7, 2025)

### ✅ Setup
- Installed Python 3
- Configured Visual Studio Code for Python development
- Installed useful extensions (Error Lens, TODO Tree, CodeSnap)
- Connected VS Code with GitHub

---

## 🗓️ Day 1 – Python Basics + Output Formatting (Aug 8, 2025)

### ✅ Concepts Learned

- Using `print()` with `sep`, `end`, and `flush` parameters
- Single-line (`#`) and multi-line (`'''...'''` or `"""..."""`) comments
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- Built-in functions: `abs()`, `round()`, `pow()`, `divmod()`
- Difference between string concatenation and numeric addition
- Typecasting: explicit and implicit conversions between `int`, `str`, `float`, `bool`, `list`, and `tuple`
- Using `input()` combined with `.split()` to read multiple inputs
- String formatting using f-strings and `.format()`
- Alignment and padding in strings using `<`, `>`, `^` with width and fill characters
- Numeric formatting to control decimal precision
- Using `flush=True` in `print()` for real-time output

---

# 📅 Day 2 – Python Strings & Operators  (Aug 9, 2025)

## ✅ What I Learned

- **Strings are immutable** (cannot be changed directly).  
- Declaring strings: `'...'`, `"..."`, `"""..."""` (multiline).  
- Access characters by index; use slicing `[start:end]`.  
- Common string methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.find()`, `.index()`, `.count()`.  
- Difference: `.find()` returns -1 if not found; `.index()` throws error.  
- Escape sequences: `\n` (new line), `\t` (tab), `\\` (backslash).  
- Raw strings `r"..."` treat backslashes literally.  
- Loop over strings with `for`.  

- **Operators:**  
  - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
  - Assignment: `=`, `+=`, `-=` etc.  
  - Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`  
  - Logical: `and`, `or`, `not`  
  - Membership: `in`, `not in`  
  - Identity: `is`, `is not`  

## 💡 Notes

- Use `.join()` to concatenate many strings efficiently.  
- Strings can’t be changed — create new strings for updates.  

---

## 🗓️ Day 3 – Python Control Flow (Aug 10, 2025)

### ✅ Concepts Learned

- **Loops**  
  - `for` loop to iterate over sequences or ranges.  
  - `while` loop for repetition until a condition is false.  

- **Conditional Statements**  
  - `if`, `elif`, and `else` for decision making.  

- **match-case**   
  - `case _` acts as a default case.   
  - Can match multiple values in a single case using `|`.  
  - Matches complex patterns like lists, tuples, and dictionaries.  
  - `_` can be used as a wildcard to ignore values.  

- **Loop Control Statements**  
  - `break` → exits loop immediately.  
  - `continue` → skips current iteration and moves to the next.  
  - `pass` → placeholder, does nothing.  

---

## 💡 Notes

- `match-case` is checked top to bottom; first match wins.
- Use `break` carefully in nested loops — it only breaks the current loop.  
- `pass` is useful when you need a syntactically valid placeholder.  

---

# 🗓️ Day 4 – Python Definitions & Patterns (Aug 11 2025) 

✅ Topics Learned  
- Loop patterns (e.g., spacing, diamond star)  
- Function definitions – with and without `return`  
- Understanding loop ranges for spaces and stars  

📂 Files Updated  
- `definition.py`  
- `practice_loop.py` (will be updated over time)  

---

# 🗓️ Day 5 – Python Practice & Revision (Aug 12, 2025)

## ✅ Today’s Work
- Practiced medium pattern problem (`number_pyramid`).
- Revised definitions of **function** and **loop**.
- Worked with nested loops for spacing and alignment.
- Explored *Book:-Automate the Boring Stuff with Python* for concept revision.


---

## 🗓️ Day -06 – Python Lists + Tuples Practice (Aug 13, 2025)

### ✅ Concepts Learned
- Lists (iteration, slicing, comprehension, methods)  
- Removing duplicates  
- Matrix traversal  
- String to list & reverse words  
- Tuples (immutable collections)  

---

### 📝 Practice
- Remove duplicates from a list     
- Matrix element printing  
- Reverse words in a sentence  
- Parallel iteration with `zip()`  
- Tuple creation and access  
- Tuple unpacking  


---

# 🗓️ Day -07 – Python Tuples & Sets (Aug 14 2025)  

✅ Topics Learned  
- Tuples: immutable, indexing, slicing, unpacking, nested tuples  
- Sets: unordered, no duplicates, looping, methods (`union`, `update`, `intersection`, `intersection_update`)  

--- 

# 🗓️ Day -08 – Python `time.strftime` Format Codes (Aug 15, 2025)

✅ **Concepts Learned**  
- Using `time.strftime()` to format date and time strings in Python.  
- Understanding various **format codes** for date/time representation.  
- Combining multiple placeholders in a single formatted string.

---

# 🗓️ Day -09 – Python Sets (Aug 16, 2025)

### ✅ Topics Learned  
- **Set Operations**: `union`, `update`, `intersection`, `intersection_update`,  
  `difference`, `difference_update`, `symmetric_difference`, `symmetric_difference_update`  
- **Set Manipulation**: `isdisjoint`, `issuperset`, `issubset`,  
  `add`, `update`, `remove`, `discard`, `pop`, `clear`, `del`, `in`  

### 🔁 Revision  
- Revised previous topics for better recall and clarity.

---

# 🗓️ Day 10 – Python Dictionaries (Aug 17, 2025)

## ✅ Today's Work
- Learn Dictionary
- Covered **12 dictionary operations**: creation, access, update, removal
- Practiced **safe access** with `.get()` vs `[]` notation
- Worked with **nested dictionaries** and **dictionary iteration**
- Learned **modern merging** with `|` operator (Python 3.9+)
- Explored `.setdefault()`, `.pop()`, `.popitem()`, and `.clear()` methods

---
