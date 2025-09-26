# 📈 Python Learning Progress Log

---

# 🗓️ Day 0 – Setup (August 7, 2025)

### ✅ Setup
- Installed Python 3
- Configured Visual Studio Code for Python development
- Installed useful extensions (Error Lens, TODO Tree, CodeSnap)
- Connected VS Code with GitHub

---

# 🗓️ Day 1 – Python Basics + Output Formatting (Aug 8, 2025)

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

# 🗓️ Day 2 – Python Strings & Operators  (Aug 9, 2025)

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

# 🗓️ Day 3 – Python Control Flow (Aug 10, 2025)

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

# 🗓️ Day -06 – Python Lists + Tuples Practice (Aug 13, 2025)

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

# 🗓️ Day 11 - basics of exception handling (Aug 18, 2025)
- basics of exception handling in pyhthon
- learn about try-except flow
- start basic of what is finally

---

# 🗓️ Day 12 – File Handling & Exception Handling (Aug 19, 2025)

## ✅ Today's Work

### File Handling
- Detailed Flow of Nested try-except-finally
- Learned how to open files using `open(filename, mode)`
- Covered file modes: `'r'` (read), `'w'` (write), `'a'` (append), `'x'` (create)
- Practiced reading file content with `.read()`
- Learned writing to files and automatic file creation
- Learned to close files properly with `.close()`
- Explored text mode `'t'` and combining modes (`'rt'`, `'wt'`)


---

# 🗓️ Day 13 – File Handling & Recursion (Aug 20, 2025)

✅ Today's Work

**File Handling**
* Learned file modes: `'r'`, `'w'`, `'a'`, `'x'` and text/binary modes
* Practiced reading with `.read()` and writing with `.write()`
* Used `with` statement for automatic file closing
* Practice: Created, wrote to, and read from sample.txt files

**Recursion**
* Understood recursion basics with end conditions
* Implemented: factorial, fibonacci, sum of digits, stair climbing ways
* Learned recursive patterns: base case + recursive relationship
* Practice: Built 5 recursive functions with dry run analysis of factorial(5)

---

# 🗓️ Day 14 - File I/O Advanced (Aug 21, 2025)
- Reviewed basics: `open()`, `close()`, file modes  
- Learned:
  - `read()`, `readline()`, and `writelines()`  
  - Iterating over file lines  
  - Writing iterable objects into files  
  - Using `seek()`, `tell()`, and `truncate()`  

---


# 🗓️ Day 15 - Python File I/O Progress – Binary Files & Integrity Check (Aug 22, 2025)

- Binary file handling** for images and audio  
- Chunked reading/writing** for large files  
- MD5 hashing** to verify file integrity
- Practice of Recursion

---

# 🗓️ Day 16 - Custom Exceptions, Short-hand If-Else, any() & all() (Aug 23, 2025)

- **Custom Exceptions**
  - Created and raised user-defined exceptions
  - Basic exception hierarchy for larger projects

- **Short-hand If-Else**
  - Learned single-line if-else syntax
  - Practiced multiple conditions in a compact format

- **any() and all() Functions**
  - Used `any()` for checking at least one condition is true
  - Used `all()` for validating multiple conditions together
  - Practical examples: input validation, password strength check

---

# 🗓️ Day 17 Expense Tracker (Project) - (24 Aug 2025)  

- **🚀 Project Completed: Expense Tracker**  
  Built a complete **command-line expense management system** with:  
  - Full CRUD Operations – Create, Read, Update, Delete expenses with category management  
  - Advanced File Handling – Temporary files + atomic writes for data safety  
  - Error Management – Custom exception handling for robust user experience
 
- **🎯 Key Learning Achievements**  
  - File I/O Mastery – Safe data persistence with backup mechanisms  
  - Data Structures – Effective use of dictionaries and lists for data management  
  - User Experience – Input validation and error handling for smooth operation

- 🔗 Project Link :- [View My Expense Tracker Project](https://github.com/er-dharmil-panchal/Python_learning/tree/main/Projects/Expense_Tracker)

---

# 🗓️ Day 18 - OOP & Classes (Aug 25, 2025)

- **OOP Basics:** Class = blueprint, Object = instance  
- **OOP Concepts:** Encapsulation, Inheritance, Polymorphism, Abstraction  
- **Methods:** Instance (`self`), Class (`cls`), Static (independent)  
- **Constructor:** `__init__` initializes objects automatically  
- **Examples:** Person, Method, GoogleCompany, Car  
- **Static Analogy:** Cleaner → belongs to class, works independently

---

# 🗓️ Day 19 - OOP Concepts: Inheritance, Encapsulation, Polymorphism (Aug 26, 2025)

- **Inheritance**
  - Child can access parent properties/methods
  - Types: Single, Hierarchical, Multilevel, Multiple
  - Method overriding, `super()` keyword

- **Encapsulation**
  - Hide data, control access
  - Public (`var`) → anywhere
  - Protected (`_var`) → class/subclass (discouraged outside)
  - Private (`__var`) → inside class only, use getter/setter

- **Polymorphism**
  - Same method behaves differently based on object
  - Method Overriding → runtime polymorphism
  - Method Overloading → default args / *args
  - Operator Overloading → customize `+,-,*,/,==,str()`

---

# 🗓️ Day 20 - OOP Concepts: Name Mangling & Decorators (Aug 27, 2025)

- **Name Mangling**
  - Prevents accidental overwrite of private variables in subclasses
  - Private attributes renamed internally → `_ClassName__var`
  - Parent and child can have separate private variables safely

- **Decorators**
  - Functions that wrap other functions to add extra functionality  
  - **Custom Decorators**
    - Basic wrapper structure using `*args` and `**kwargs`
    - Used for logging, validation, etc.
  - **Inbuilt Decorators**
    - `@property` / `@<property>.setter` → for controlled getters & setters  
    - `@staticmethod` → method tied to class, not object  
    - `@classmethod` → method tied to class, often used for factory methods  

- **Key Takeaways**
  - `__var` is not truly private, but safely isolated per class
  - Decorators help add functionality without touching original code
  - Learned usage of logging, authentication checks, and property management
---

# 🗓️ Day 21 – Python Variable Types (Aug 28, 2025)

## Instance & Class Variables
- **Instance Variables** → defined inside `__init__()`, unique to each object  
- **Class Variables** → defined at class level, shared among all instances  
- Mutable class variables (list/dict) are shared across instances  

## Local & Global Variables, and  OOP Revision
- **Local Variables** → defined inside a function, accessible only there  
- **Global Variables** → defined outside functions/classes, accessible everywhere  
- Use `global` keyword to modify global variables inside functions  
- **Nonlocal Variables** → modify variables in outer function from nested function (`nonlocal`)  
- OOP concept revision

---

# 🗓️ Day 22 – Python Imports & OS Module (Aug 29, 2025)

## Import Basics
* Learned `import`, `from ... import`, and `as` for aliases  
* Used `dir()` to explore available module attributes  
* Practiced with `math` for radians, sine, cosine, and powers  

## Custom Modules
* Imported user-defined scripts and avoided running extra code using `__name__ == "__main__"`  
* Practiced reloading updated modules without restarting the script

## OS Module
* Used `os.getcwd()` to get the current working directory  
* Created and removed folders with `os.mkdir()` and `os.rmdir()`  
* Listed files in a directory using `os.listdir()`  
* Learned path handling basics for cross-platform code

---

# 🗓️ Day 23 - Python JSON  (Aug 30, 2025)

- JSON basics , importance , rules & value types
- Reading/writing JSON files (`json.load`, `json.dump`, `json.loads`, `json.dumps`)
- Updating/appending JSON data
- Exception handling
- Accessing nested JSON safely
- Serializing custom Python objects
- JSON Schema validation
- Merging JSON files
- Working with large JSON files (`ijson`)
- Faster JSON serialization (`orjson`)

---

# 🗓️ Day 24 - Python CSV (Aug 31, 2025)

- CSV basics: structure, usage, and differences from JSON  
- Reading CSV files with `csv.reader` and `csv.DictReader`  
- Writing CSV files with `csv.writer` and `csv.DictWriter`  
- Appending data (list-based and dict-based methods)  
- Updating and deleting rows by reading and rewriting  
- Sorting CSV data using custom keys

---

# 🗓️ Day 25 – Basics of Functional Programming (Sep 1, 2025)

## Introduction
* Explored the concept of **Functional Programming** in Python  
* Learned how functions can be treated as first-class citizens  
* Practiced creating **pure functions** and using **lambdas** for concise code  

## Core Tools & Techniques
* **`map()`** – applied transformations to lists and other iterables  
* **`filter()`** – extracted data matching specific conditions  
* **`reduce()`** – combined sequences into a single result (like sums or products)  
* Learned how to **chain tools** like `map+filter`, `map+reduce`, `filter+reduce`, ans `map+filter+reduce` for complex operations  
* Practiced **`zip()`** and **`enumerate()`** for pairing data and working with indexes  

## Comprehension Revision
* Revisited **list, set, and dictionary comprehensions** for concise data manipulation  
* Practiced **nested comprehensions** and adding conditions  
* Learned **generator expressions** for **memory-efficient iteration**  
* Compared **memory usage** between lists and generators with large datasets  

---

# 🗓️ Day 26 – Functools & JSON-CSV Conversion (Sep 2, 2025)

## Functools Module
* Learned about the `functools` module for higher-order functions and function manipulation
* Used **partial functions** to pre-fill arguments and avoid repetition in callbacks or loops
* Revised **reduce** for sequence aggregation
* Implemented **lru_cache** for caching results and improving performance in recursive functions like Fibonacci
* Learned **wraps** to preserve function metadata (`__name__`, `__doc__`) when building decorators
* Used **total_ordering** to auto-generate missing comparison methods in classes
* Practiced **cmp_to_key** for custom sorting with comparator functions

## JSON ↔ CSV Conversion
* Converted **JSON to CSV** using `csv.DictWriter`, including writing headers and multiple rows
* Converted **CSV to JSON** using `csv.DictReader` and processed numeric fields for type accuracy
* Understood the practical workflow for **data transformation** between formats for structured processing

---

# 🗓️ Day 27 – Virtual Environments & requirements.txt (Sep 3, 2025)

## Virtual Environments
* Learned to **create, activate, deactivate, and delete venvs**
* Practiced installing packages inside isolated environments
* Understood managing **multiple environments** per project in PyCharm

## requirements.txt
* Created and updated `requirements.txt` with `pip freeze`
* Installed dependencies quickly with `pip install -r requirements.txt`
* Learned its role in **reproducibility and version control**

---

# 🗓️ Day 28 – Python Dunder Methods (Sep 4, 2025)

- `dir()` – list all attributes & methods of an object  
- `__dict__` – dictionary representation of an object’s instance attributes  
- `help()` – show documentation of any object (class, method, module)  
- Dunder/Magic methods (`__init__`, `__str__`, `__repr__`, `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__next__`, `__call__`, `__contains__`, `__del__`, `__enter__`, `__exit__`)  
- Context manager support with `__enter__` and `__exit__`  
- Object callable using `__call__`  
- Iteration protocol using `__iter__` and `__next__`  

---

# 🗓️ Day 29 – Mini Social Network (Sep 5 2025)  
# 🚀 Project Started: Mini Social Network  

## Began building a **command-line social network** in Python with:  
- **User Registration & Login** – Secure login system with SHA-256 password hashing  
- **Profile Management** – Basic profile setup with username, age, and bio  
- **Post Creation** – Ability to create posts with title, content, and timestamps  
- **Persistent Storage** – Data stored in `users.json` and `posts.json` for reliability  
- **Schema Validation** – Integrated `jsonschema` for consistent and valid data  

## 🎯 **Key Learning Achievements**  
- Modular Project Design – Clean separation with `Main.py`, `user.py`, `Post.py`, and `Util.py`  
- JSON File Handling – Read/write operations for persistent storage  
- Data Validation – Learned to enforce structure with `jsonschema`  
- CLI Workflow – Menu-driven interface with Python’s `match-case`  

---

# 🗓️ Day 30 – Mini Social Network (Sep 6 2025)  
# 🚀 Project Update: Follow/Unfollow & Social Feed

## Began enhancing **social interactions** in the CLI social network:  
- **Follow/Unfollow System** – Users can follow/unfollow others; stored in `followers.json`  
- **Dynamic Feed** – Followed users’ posts appear first, sorted by most recent  
- **Profile Improvements** – Last 5 posts visible; follow/unfollow button integrated  
- **Input Validations & CLI Enhancements** – Prevent following self and duplicates; cleaner menus

## 🎯 **Key Learning Achievements**  
- Built social interaction logic in CLI  
- Practiced JSON file handling for followers  
- Implemented feed prioritization and improved user experience

---

# 🗓️ Day 31 – Python Multi-Threading Basics (Sep 7, 2025)

- Learned **threads** as smallest unit of execution  
- Practiced **multithreading** for concurrent tasks  
- Used `threading.Thread` with functions  
- Learned `start()` vs `join()` to control execution  
- Explored **thread information**: `current_thread()`, `active_count()`, `enumerate()`  
- Learned storing results from threads using **shared list/dict**  
- Basic **thread states**: New, Runnable, Running, Waiting/Blocked, Terminated

---

# 🗓️ Day 32 – Python Class-Based Threads, Daemons & Synchronization (Sep 8, 2025)

- Learned creating **custom threads** by subclassing `threading.Thread`  
- Explored **daemon threads** vs normal threads  
  - Daemon threads → background, killed when main program exits  
  - Checked daemon status using `.daemon` attribute  
- Learned about **race conditions** and why they occur  
- Fixed race conditions using **Lock()** and context manager (`with lock`)  
- Understood **RLock (Reentrant Lock)** for recursive acquisitions  
- Practiced **Semaphore** to limit concurrent threads  
- Used **Condition (wait/notify)** for Producer-Consumer pattern  
- Studied **Deadlocks** and ways to prevent them (consistent order, timeout)

**Note:** Practice exercises on multithreading will be added soon.

---

# 🗓️ Day 33 – NumPy Basics & Operations (Sep 9, 2025)

## Introduction & Setup
* Learned what **NumPy** is and why it’s faster than Python lists
* Created first array and checked attributes (`shape`, `ndim`, `dtype`, `size`)

## NumPy Basics
* Practiced creating arrays using:
  - `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
* Explored array attributes (`shape`, `dtype`, `ndim`, `size`)
* Performed indexing & slicing on **1D and 2D arrays**
* Learned to **reshape arrays** and understood axes

## Array Operations
* Performed arithmetic operations (**add, subtract, multiply, divide**)
* Understood **broadcasting rules** with scalars and arrays
* Used universal functions (`np.sqrt`, `np.exp`, `np.log`)
* Practiced aggregation functions (`np.sum`, `np.mean`, `np.max`, `np.min`, `np.std`)
* Learned about NumPy **data types** (`int`, `float`, `bool`, `complex`, `string`, `datetime`, `object`, etc.)

---

# 🗓️ Day 34 – NumPy Advanced Indexing & Random Module (Sep 10, 2025)

## Advanced Indexing & Slicing
* Learned **Boolean Indexing** to filter arrays with conditions
  - Single condition, multiple conditions using `&`/`|`, negation with `~`
* Practiced **Fancy Indexing** with custom index arrays (1D & 2D)
* Explored **np.where()** for vectorized conditional selection/replacement

## Random Module
* Generated **random integers** using `np.random.randint()`
* Generated **random floats** using `np.random.rand()`, `np.random.random()`, `np.random.uniform()`
* Picked elements randomly using **np.random.choice()** (with/without replacement, weighted probabilities)
* Explored **random distributions**
  - Standard Normal (`np.random.randn`)
  - Custom Normal (`np.random.normal`)
  - Binomial Distribution (`np.random.binomial`)
* Shuffled arrays using **shuffle** and **permutation**
* Used **seed** for reproducibility

---

# 🗓️ Day 35 – NumPy Linear Algebra & Useful Functions (Sep 11, 2025)

## Linear Algebra – `numpy.linalg`
* **Dot Product & Matrix Multiplication**: `np.dot()`, `@`
* **Transpose**: `.T`
* **Determinant**: `np.linalg.det()` (check invertibility)
* **Inverse**: `np.linalg.inv()` (or pseudo-inverse with `np.linalg.pinv()`)
* **Eigenvalues & Eigenvectors**: `np.linalg.eig()`, `np.linalg.eigh()`, `np.linalg.eigvals()`
* **Solving Linear Systems**: `np.linalg.solve()`
* **Matrix Norms**: `np.linalg.norm()` (Euclidean, Frobenius, ord=1, ord=inf)
* **Trace**: `np.trace()`
* **Matrix Rank**: `np.linalg.matrix_rank()`
* **Condition Number**: `np.linalg.cond()`
* **Kronecker Product**: `np.kron()`

## Useful NumPy Functions
* **Unique Elements**: `np.unique()` (with `return_counts`, `return_index`, `return_inverse`)
* **Sorting**: `np.sort()`, `np.argsort()`, sorting by axis, flattened sort
* **Stacking Arrays**: `np.hstack()`, `np.vstack()`, `np.stack()`, `np.column_stack()`, `np.dstack()`, `np.concatenate()`
* **Splitting Arrays**: `np.split()`, `np.array_split()`, `np.hsplit()`, `np.vsplit()`
* **Searching**: `np.where()`, `np.nonzero()`, `np.argwhere()`, `np.any()`, `np.all()`, `np.searchsorted()`

*💡 Do some practice to solidify concepts.*

---

# 🗓️ Day 36 – NumPy Real Data, Cleaning & Scaling (Sep 12, 2025)

* Loaded messy numeric data using `np.loadtxt()` (simple, numeric only) and `np.genfromtxt()` (handles NaNs).
* Checked and located NaNs with `np.isnan()` and `np.where()`.
* Explored NaN handling with `np.nansum()`, `np.nanmean()`, `np.nanstd()`.
* Replaced NaNs using `np.nan_to_num()` or column means via `np.take()`.
* Cleaned data by removing rows with NaNs, duplicates (`np.unique()`), and invalid values; applied conditional feature filtering.
* Understood fancy indexing vs `np.take()` (axis control, flattened indexing, out-of-range handling with `clip` or `wrap`)—useful for NaN replacement and column-wise operations.
* Learned scaling techniques: normalization (0–1 range, preserves order) and standardization (mean=0, std=1, accounts for variability) in **detail**.

💡 Practiced combining these steps for real-world datasets to ensure clean, scaled, ML-ready data.

---

# 🗓️ Day 37 – NumPy Advanced Topics & Image Manipulation (Sep 13, 2025)

## NumPy - Advanced Topics
* **Broadcasting**: performed operations on arrays of different shapes without explicit loops.
* **Vectorization**: fast, loop-free numerical operations using NumPy.
* **Memory Layout**:
  - Views vs Copies: slicing creates views, `.copy()` creates independent arrays.
* **Performance Comparison**: NumPy arrays faster than Python lists for arithmetic, aggregation, and mathematical operations.
* **Structured Arrays**: stored heterogeneous data with field names, accessed via `data['field_name']`.
* **Iteration with `nditer`**: flexible, memory-efficient iteration across multi-dimensional arrays; supports in-place modifications and broadcasting.
* **Trigonometric & Mathematical Functions**: `np.sin()`, `np.cos()`, `np.tan()`, `np.sqrt()`, `np.exp()`, `np.log()`, `np.trunc()`.
* **Statistical Functions**: `np.percentile()`, `np.corrcoef()`, `np.histogram()` for percentiles, correlations, and histograms.

## Image Manipulation Practice
* Loaded an image using `PIL.Image` and converted it to a NumPy array.
* Explored image shapes: `(height, width, channels)` → confirmed RGB layout.
* Converted image to **grayscale** using `img_array.mean(axis=2).astype(np.uint8)`.
* Applied **single-channel filters**:
  - Red, Green, Blue isolation by zeroing out other channels.
* Created **custom color images** using user-provided multipliers for RGB channels.
* Cropped images using slicing: `cropped_array = img_array[y1:y2, x1:x2]`.
* Adjusted **brightness** using broadcasting: `np.clip(img_array + bright_val, 0, 255)`.

---

# 🗓️ Day 38 – NumPy Project – Student Performance Analysis (Sep 14, 2025)

##  Overview
Analyze 100-student dataset using **NumPy**: load, clean, manipulate, compute stats, sort, filter, and calculate correlations.

##  Features
- **Load CSV** → User input or default file  
- **Clean Data** → Remove duplicates, handle missing values (`np.nan`)  
- **Convert Numeric** → Scores & attendance as float  
- **Manipulate Data** → Bonus marks, normalize attendance  
- **Statistics** → Mean, Std, top student total  
- **Filtering** → Students with 80+ in all subjects  
- **Sorting** → Top 5 students by total marks  
- **Linear Algebra** → Weighted average, correlation matrix

---

# 🗓️ Day 39 – Pandas Basics & Data Selection (Sep 15, 2025)

## Pandas Basics
* Learned what **Pandas** is and why it is built on NumPy  
* Created **Series** (from list, dict, scalar) and explored attributes (`index`, `values`, `dtype`, `head`, `tail`)  
* Created **DataFrames** (dict of lists, list of lists, NumPy array)  
* Practiced inspecting data with `head()`, `tail()`, `shape`, `info()`, `describe()`, `dtypes`  
* Loaded and saved data using `read_csv()`, `to_csv(index=False)`, `read_json()`, `to_json()`

## Data Selection & Indexing
* Selected **columns** (single → Series, multiple → DataFrame)  
* Selected **rows** with `loc[]` (label) and `iloc[]` (position)  
* Combined row + column selection  
* Practiced **row/column slicing** (loc inclusive, iloc exclusive)  
* Used **boolean indexing** for filtering (`df[df['Age']>18]`)  
* Created, updated, and dropped columns using vectorized operations

---

# 🗓️ Day 40 – Pandas Data Cleaning (Sep 16, 2025)

* Learned how to **detect missing values** with `isnull()` / `isna()` and count them  
* Practiced **filling missing data** with constants, median (numeric), and mode (categorical)  
* Understood `errors='coerce'` in `pd.to_numeric()` and converted invalid data to NaN safely  
* Preserved numeric columns using `.astype('Int64')`  
* Cleaned string columns by trimming spaces (`.str.strip()`) and fixing case (`.str.capitalize()`)  
* Standardized city names and replaced blanks with `"Unknown"`  
* Learned to **drop duplicates** after cleaning to remove exact matches  
* Practiced dropping rows with missing values using `dropna(subset=['Age'])`

---

# 🗓️ Day 41 – Pandas Filtering, Sorting & Ranking (Sep 17, 2025)

* Recapped **Boolean filtering** and used multiple conditions with `&` (AND) and `|` (OR)  
* Practiced `isin()` for list-based filtering and `between()` for range-based filtering  
* Learned **SQL-like syntax** with `query()` and used variables inside queries with `@`  
* Used `.loc[]` to filter rows and select specific columns safely  
* Performed string-based filtering with `.str.contains()`, `.str.startswith()`, `.str.endswith()`  
* Learned difference between **chained indexing** vs using `.loc` (best practice)  
* Practiced `sort_values()` (single & multiple columns, ascending/descending)  
* Sorted rows by index with `sort_index()`  
* Learned to reset index after sorting with `reset_index(drop=True)`  
* Used `rank()` to assign positions based on column values and explored ranking methods:  
  * `average`, `min`, `max`, `dense` (handling ties)  
* Combined filter → sort → head() to get **top-N results** (real-world analysis)

---

# 🗓️ Day 42 – Pandas GroupBy & Aggregation (Sep 18, 2025)

* Learned **Split → Apply → Combine** concept with `groupby()`  
* Grouped by single/multiple columns and applied `mean`, `sum`, `count`, `min`, `max`  
* Used `.agg()` for multiple aggregations and **named aggregation** for readability  
* Accessed groups with `.groups` / `.get_group()` and filtered groups with `.filter()`  
* Learned **top-N per group** (`nlargest()`) and **custom functions** via `.apply()`  
* Used `.transform()` for group-wise operations and **cumulative operations** (`cumsum`)  
* Flattened multiIndex columns with `.reset_index()` and practiced **pivot tables**  

---

# 🗓️ Day 43 – Pandas Joining & Merging (Sep 19, 2025)

* Learned **SQL-style joins** (`inner`, `left`, `right`, `outer`) using `pd.merge()`  
* Merged DataFrames with **different column names** using `left_on` / `right_on`  
* Joined DataFrames on **index** using `join()` and controlled overlaps with `lsuffix` / `rsuffix`  
* Merged on **multiple keys** (composite keys) for precise matching  
* Handled **overlapping column names** with `suffixes`  
* Stacked DataFrames **vertically** and **horizontally** using `pd.concat()` and `keys` for MultiIndex  
* Filled missing data from another DataFrame using `combine_first()`  
* Debugged joins with `indicator=True` to see row origin (`left_only`, `right_only`, `both`)

---

# 🗓️ Day 44 – Pandas Apply & Transform (Sep 20, 2025)

* Used `.apply()` for **row-wise and column-wise** operations (custom calculations & lambda functions)  
* Used `.map()` for **Series-level transformations**, including **dict-based mapping**  
* Used `.applymap()` for **element-wise operations** on entire DataFrame  
* Performed **group-wise transformations** with `.transform()` (broadcast group mean to rows)  
* Created **custom features** (total marks, difference from group mean) using `apply` and `transform`  
* Learned **differences** between `apply`, `map`, `applymap`, and `transform`  
* Understood why **vectorized operations are faster** than apply and when to prefer them  

---

# 🗓️ Day 45 – Pandas Time Series & Data-Handling (Sep 21, 2025)

* Converted columns to **datetime** and extracted components (year, month, day, etc.)  
* Set **DatetimeIndex** for easy selection and partial string indexing  
* Filtered rows using **boolean masks** on date components  
* **Resampled** data daily, weekly, monthly with `.resample()`  
* Used **.shift()** for lag/lead comparisons  
* Calculated **rolling/moving averages** and compared with previous periods  
* Handled **time zones** with `tz_localize()` and `tz_convert()`  
* Sorted by datetime to ensure correct rolling/resampling results  

---

# 🗓️ Day 46 – Pandas Business Days & Offsets (Sep 22, 2025)

* Learned to generate **business-day ranges** using `pd.bdate_range()` (Mon–Fri only)  
* Shifted sales values by **business days** using `.shift(freq="B")`  
* Added **future business-day offsets** with `pd.offsets.BDay()` for forecasting  
* Understood practical applications in **finance, sales, and delivery date projections**  
* Did some **practice and revision** of Pandas concepts to prepare for the final project

---

# 🗓️ Day 47 – Matplotlib Line Plot Customization (Sep 23, 2025)

* Created **basic line plots** using `plt.plot()`  
* Added **title, x-axis and y-axis labels**, and **grid** for better readability  
* Customized **lines**: color, linestyle, linewidth, alpha  
* Customized **markers**: type, size, face color, edge color  
* Added **legend** to identify plots  
* Saved figures as **PNG and PDF** using `plt.savefig()`  
* Practiced Matplotlib basics and maintained
* **consistent daily progress, covering topics gradually due to festival**

---

# 🗓️ Day 48 – Matplotlib Various Plot Types (Sep 24, 2025)

* Learned **Bar Plots**: vertical, horizontal, grouped, stacked  
* Learned **Scatter Plots** and customization: color, size, marker, edge color, alpha  
* Learned **Histograms**: bins, density, multiple datasets, annotations  
* Learned **Pie Plots**: proportions, autopct, explode, labels  
* Learned **Area Plots**: basic area, multiple areas, baseline area  
* Practiced various plot types to enhance data visualization skills  

---

# 🗓️ Day 49 – Matplotlib Styling & Customization (Sep 25, 2025)

* Axis control: setting limits, aspect ratios, tight/equal scaling  
* Ticks customization: major & minor ticks, locators, formatters, rotation  
* Legends: adding, positioning, styling  
* Colors & styles: linestyles, markers, alpha, style sheets  
* Text & annotations: plt.text(), plt.annotate()  
* Axis vs Axes: difference and usage  
* Practiced customization techniques for making plots presentation-ready  

---

# 🗓️ Day 50 – Matplotlib Multiple Plots & Subplots (Sep 26, 2025)

* Multiple lines in one figure: repeated `plt.plot()` calls, labels, colors, linestyles
* Subplots with `plt.subplot()`: creating grids, independent titles, labels, limits
* Subplots with `plt.subplots()`: `fig` and `ax` objects, shared axes, explicit control
* Global customization: `fig.suptitle()`, `fig.text()` for common labels
* Layout control: `plt.tight_layout()`, `plt.subplots_adjust()`
* Practiced subplot creation, axis sharing, loop automation, and layout adjustment
