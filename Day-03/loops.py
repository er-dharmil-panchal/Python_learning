# ==========================================================================================================
# ==========================================================================================================
# ------------------------------------------------ LOOPS ---------------------------------------------------
# ==========================================================================================================
# ==========================================================================================================

"""
Printing 1 to 5 is easy using print method,
but printing 1 to 20,000 using print repeatedly is time-consuming.
Using loops makes this easy and efficient.
"""

# ==========================================================================================================
# ------------------------ 👉🏻 FOR LOOP 👈🏻 ------------------------
# ==========================================================================================================

name = "Dharmil"

for j in name:
    print(j)
    # Syntax: for <iterator> in <variable>:
    # 'j' takes each character of 'name' one by one: 'D', 'h', 'a', ...

for j in name:
    print(j, end=",")  # prints characters separated by commas

print("\n\n")

for i in name:
    print(i)
    if i == "m":
        print("This is special character")
        # Prints this line right after character 'm' is printed


# For loop in LIST

colors = [
    "Red",
    "Pink",
    "Blue",
    "Green",
    "Yellow",
]

for i in colors:
    print(i)

print("\n\n")

# You can also do this:
for color in colors:
    print(color)
    # Print each character of the string in the list
    for i in color:
        print(i)
        # Output: R e d then P i n k and so on


# -------> RANGE function in for loop
# Range works with integers (not strings)

for k in range(5):
    print("Dharmil", k + 1)  # Note: k starts from 0

for k in range(1, 9):
    print(k)
    # Output: 1 2 3 4 5 6 7 8 (start is inclusive, end is exclusive)

print("\n\n")

# STEP argument in range

for k in range(1, 12, 2):
    print(k)
    # Output: 1, 3, 5, 7, 9, 11 (step of 2)

for k in range(1, 12, 3):
    print(k)
    # Output: 1, 4, 7, 10 (step of 3)


# ==========================================================================================================
# ------------------------ 👉🏻 WHILE LOOP 👈🏻 ------------------------
# ==========================================================================================================

# You can write while condition without parentheses

print("\n\n\n")

i = 1
while i <= 3:
    print(i)
    i = i + 1
    # This is an incrementing loop
    # While loop works similar to for loop but syntax differs
    # Forgetting to increment/decrement may cause infinite loop


i = int(input("Enter the number: "))
j = 1
while j <= i:
    print(j)
    j = j + 1


# NOTE: Decrementing Loop

count = 5
while count > 0:
    print(count)
    count = count - 1

print("\n\n")


# -------> ELSE with WHILE LOOP

"""
If while condition becomes False, then else block runs.
"""

count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("While-loop condition became False, so ELSE block executed")


# ==========================================================================================================
# ------------------------ 👉🏻 DO-WHILE LOOP (emulation) 👈🏻 ------------------------
# ==========================================================================================================

"""
In languages like Java, C, C++, there's a 'do-while' loop
which executes the loop body at least once.
"""

# Python doesn't have built-in do-while loop.
# Emulate do-while using while True + break:

i = int(input("Enter the number (End with 11): "))
while i <= 10:
    i = int(input("Enter the number (End with 11): "))

"""
This tries to emulate do-while, but
if loop body is very long, this duplicates code and is not efficient.

Learning 'break' and 'continue' is necessary for better emulation.
"""

# -------> Emulating do-while loop

# Print 1 to 100 using do-while style

i = 0
while True:  # infinite loop
    print(i)
    i = i + 1
    if i == 101:
        break  # exit loop when i reaches 101

while True:
    n = int(input("Enter Positive Number:-- "))
    print(n)
    if not n > 0:
        print("It is a Negative Number")
        break


# ==========================================================================================================
# ------------------------ 👉🏻 LOOP ELSE CLAUSE (for loop) ------------------------
# ==========================================================================================================

for i in range(5):
    print(i)
else:
    print("Loop completed without break")

for i in range(5):
    if i == 3:
        break
else:
    print("This won't print because loop was broken")

# ==========================================================================================================
# ------------------------ 👉🏻 PASS vs CONTINUE (Basic Difference) ------------------------
# ==========================================================================================================

"""
'pass' and 'continue' are NOT the same, though sometimes their output might look similar.

pass      → Does nothing. Just a placeholder to keep the code syntactically correct.
continue  → Skips the rest of the loop body and jumps to the next iteration.
            (We will learn 'continue' in detail later.)
"""

# Example of pass
#NOTE :- it's more for developer for TODO later.
for num in range(3):
    if num == 1:
        pass  # Does nothing, loop still runs remaining code
    print(f"pass example num = {num}")

# Example of continue (PREVIEW ONLY)
for num in range(3):
    if num == 1:
        continue  # Skips printing for this iteration
    print(f"continue example num = {num}")

"""
Output:
pass example →
pass example num = 0
pass example num = 1
pass example num = 2

continue example →
continue example num = 0
continue example num = 2
"""


# ==========================================================================================================
# ------------------------ 👉🏻 NESTED LOOPS ------------------------
# ==========================================================================================================

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")


# ==========================================================================================================
# ------------------------ 👉🏻 COMMON LOOP PITFALLS ------------------------
# ==========================================================================================================

# Infinite loop example (avoid)
# i = 0
# while i < 5:
#     print(i)
#     # i is never incremented - infinite loop!

# Off-by-one example
for i in range(5):  # Prints 0 to 4, not 5
    print(i)




# Combined Example: break, continue, pass

for i in range(1, 8):
    if i == 3:
        pass  # Placeholder, does nothing (maybe logic will be added later)
        print("Pass at", i)
    elif i == 5:
        print("Continue at", i)  # Skip the rest of this iteration
        continue
    elif i == 7:
        print("Break at", i)  # Stop the loop completely
        break
    
    print("Number:", i)

print("Loop ended.")


# 📌 Important:
# - Code after 'pass' in the same block WILL run (pass just does nothing).
# - Code after 'break' or 'continue' in the same block will NEVER run → Python will give "unreachable code" error.
#   Example:
#   break
#   print("This will not run")  # ❌ Unreachable
