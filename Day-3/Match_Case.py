# ==========================================================================================================
#                                          Match Case Statement
# ==========================================================================================================

'''
To implement switch-case like behavior, similar to if-else,
Python uses the match-case statement (introduced in Python 3.10).

If you come from C, C++, or Java-like languages, you may know switch-case statements.

A match statement compares a variable's value to different patterns (shapes),
and executes the block of the first matching pattern.

Syntax:

match variable_name:
    case pattern1:       # statement1
    case pattern2:       # statement2
    ...
    case patternN:       # statementN
'''

# ------------------------------------------------------------------------------------------
# Basic matching: first matching case runs, lower cases are skipped after a match

x = 4
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 4:
        print("x is four")  # Output: x is four

# ------------------------------------------------------------------------------------------
# Using input and default case with '_'

x = int(input("Enter the value of x = "))
match x:
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case _:  # Default case if no other matches
        print("This is a Default statement")

# ------------------------------------------------------------------------------------------
# Adding guard conditions (if inside case)

x = int(input("Enter the value of x = "))
match x:
    case 1:
        print("x is one")
    case 2 if x <= 0:
        print("x is two and negative")  # Will only run if x is 2 and <= 0
    case 2 if x >= 0:
        print("x is two and positive")  # Will only run if x is 2 and >= 0

# ------------------------------------------------------------------------------------------
# Summary with multiple conditions and default

x = 9
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    case _ if x < 10:
        print("x is < 10")
    case _:
        print(x)  # Default case

# ------------------------------------------------------------------------------------------
# Matching multiple values in one case with '|'

x = int(input("Enter number = "))
match x:
    case 0 | 1 | 2:
        print("same answer for - 0|1|2")

# ------------------------------------------------------------------------------------------
# Matching complex patterns: lists, tuples, dictionaries

# Test with a list
value = [1, 2]  
# value = ("apple", "banana")      # Test with a tuple
# value = {"name": "Dharmil"}      # Test with a dict

match value:
    case [x, y]:  # Matches a list or tuple with exactly 2 elements
        print(f"List or tuple of length 2 with elements {x} and {y}")
    case {"name": n}:  # Matches a dictionary with a 'name' key
        print(f"Dict with name={n}")
    case _:
        print("No match")

# ------------------------------------------------------------------------------------------
# Binding variables in patterns (tuples example)

point = (1, 2)
match point:
    case (x, y):
        print(f"Point at coordinates ({x}, {y})")

# Ignoring parts of the pattern using wildcard '_'

point = (1, 2)
match point:
    case (x, _):
        print(f"X coordinate is {x}, Y is ignored")

# ------------------------------------------------------------------------------------------
# Matching list with variable-length tail using '*rest'

my_list2 = [5, 15, 25, 13, 26]
match my_list2:
    case [x, *rest]:
        print(f"First: {x}, rest: {rest}")

# ------------------------------------------------------------------------------------------
'''
Summary:

- Multiple values can be matched in one case using | (OR) operator.
- Patterns can match complex structures like lists, tuples, dicts, or objects.
- Variables can be bound to parts of the pattern for use inside the case block.
- The wildcard '_' can be used to ignore parts of a pattern.
- Patterns are checked in order; the first match executes.
- Use 'case _' as the default case; it must be last.
'''
