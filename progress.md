# 📈 Python Learning Progress Log

---

## 🗓️ Day 0 – Setup (August 7, 2025)

### ✅ Setup
- Installed Python 3
- Configured Visual Studio Code for Python development
- Installed useful extensions (Error Lens, TODO Tree, CodeSnap)
- Connected VS Code with GitHub

📄 [`String.py`](operators_notes.py)

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

# 📅 Day 2 – Python Strings & Operators

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

