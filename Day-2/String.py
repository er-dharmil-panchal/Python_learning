# ==========================================================================================================
#                                              STRING
# ==========================================================================================================

# --->  STRING ARE IMMUTABLE
name = "Dharmil"
# Trying to change the first character:
# name[0] = 'd'  # This will cause an error!

# Instead, we can create a new string:
new_name = "d" + name[1:]  # "dharmil"


# WE CAN ADD STRING USING " " ;
Name1 = "Dharmil"
# OR USE ' ' TO ADD STRING ;
Name2 = 'dharmil'
# Also we can use """ """ for long texts like ;
text = """Hi,
        my name is dharmil
        and i am learnig python 😉
"""

print("Hello " + Name1)
print(Name2)
print("Text ", text)


x = " He said,\"he wants to eat apple\""
# IF YOU WANT TO ADD "" IN STRING YOU HAVE TO USE BACK SLASH (\) ;
print(x)
x = ' He said,"he wants to eat apple"'
# OR USE '' SO YOU CAN ADD " IN YOUR STRING ;
print(x)

"""
Similarly,
\n  -> New line (moves cursor to next line)
\\  -> Backslash character (\)
\'  -> Single quote character (')
\t  -> Tab space (adds horizontal tab)
"""


# --> Extra
#r is mainly for handling backslashes \ literally in strings.
#Useful for Windows paths, regex patterns, or any text with lots of backslashes.
print("Hello\nPython")
print(r"hello\nPython")     # \n stays as two characters '\' and 'n'

# ==========================================================================================================
#                                   👉🏻Accessing Characters of a String👈🏻
# ==========================================================================================================


z = "DHARMIL"
# IN "Z" THERE ARE 7 {[0,1,2,3,4,5,6]} Character {[D,H,A,R,M,I,L]} ,String Character start with 0

print(z[0])  # ans = D
print(z[5])  # ans = I


# 👉🏻 Formatted String

fname = "Dharmil"
lname = "Panchal"
full = fname + " " + lname      #❌ less preferred
full2 = f"{fname} {lname}"      #✅ formatted string (f-string)

print(full)          
print(full2)

dummy = f"{2+2} {len(fname)}"
print(dummy )


# ==========================================================================================================
#                                          👉🏻FOR LOOP FOR STRING👈🏻
# ==========================================================================================================


y = """
 Hey!! , My name is Dharmil,
 This is a Multi-Line String.
"""

# FOR LOOP CAN GIVE EVERY SINGLE CHARACTER OF STRING , IT'S USEFUL FOR MULTI-LINE STRINGS;
for character in y:
    print(character)


# ==========================================================================================================
#                                 👉🏻STRING SLICING & OPERATIONS ON STRING👈🏻
# ==========================================================================================================


fruit = "Mango"
print(len(fruit))
# WE CAN FIND THE LENGTH OF STRING USING "len()" ;
print("Mango have ", len(fruit), "letters")

print(fruit[0])

names = "Mohit,Harry,Ram"
print(names[0:4])
# The Box Is for Range Of Character In String ;
# So [0:4] It Means indices {0,1,2,3} → characters {M,o,h,i} (4 is excluded)

print(names[1:4])  # Ans = ohi
print(names[2:4])  # Ans = hi
# '4' is the stop index and is NOT included

print(names[:4])    # -> Mohi (start defaults to 0)
print(names[4:])    # -> t,Harry,Ram (goes to end)
print(names[:])     # -> Mohit,Harry,Ram (full string)

# Negative Slicing
print(fruit)
print(fruit[0:-3])
print(fruit[0: len(fruit) - 3])
# This means index from 0 up to length minus 3 → here 5 - 3 = 2

print(fruit[-1:-3])
# [-1:-3] is like [4:2] (start index higher than stop index) so no output

print(fruit[-3:-1])
# This means [2:4] → 'ng'


# ==========================================================================================================
#                                            👉🏻STRING METHODS👈🏻
# ==========================================================================================================


# Note: String methods return new strings, original strings remain unchanged

ex = "dharmil"
ab = "1111Dharmil1111"
txt = "my name is dharmil"

# -->   # WE CAN FIND THE LENGTH OF STRING USING "len()" 
print(len(ex))

# -->   # WE CAN CONVERT STRING TO UPPERCASE USING "name.upper()" ;
print(ex.upper())

# -->   # WE CAN CONVERT STRING TO LOWERCASE USING "name.lower()" ;
print(ex.lower())
print(ab.lower())
# "1111" stays same, only alphabetic characters change

# -->   # txt.title() converts first letter of each word to uppercase
print(txt.title())          # -> My Name Is Dharmil

# -->   # We can remove leading and trailing whitespace using strip()
print("         PY".strip())

# -->   # name.lstrip() removes whitespace or specified chars from left
print("         JAVA".lstrip())
print(ab.lstrip("1"))   # -> Dharmil1111

# -->   # name.rstrip() removes whitespace or specified chars from right
print("         JAVA".rstrip())
print(ab.rstrip("1"))   # -> 1111Dharmil


# -->   # WE CAN REPLACE STRING PARTS USING "name.replace('before','after')"
print(ex.replace("d", "M"))  # case sensitive; "d" → "M"
print(ab.replace("1111", "Me"))
# All occurrences replaced


# -->   # WE CAN SPLIT STRING USING "name.split('delimiter')" ;
# NOTE: empty string ("") is not a valid delimiter for split()
c = "<<< Dharmil 123 Panchal >>>"
print(c.split(" "))
# Output: ['<<<', 'Dharmil', '123', 'Panchal', '>>>']

list_c = c.split()
print(list_c)


# -->   # WE CAN CAPITALIZE A STRING USING "name.capitalize()"
cap = "mY naME is dhArmil , i AM leaRninG pyThoN"
print(cap.capitalize())
# Output: My name is dharmil , i am learning python ;


# -->   # CENTER METHOD :- "name.center(width)"
p = "the world is circle"
print(p.center(50))
# Pads string with spaces so total length is 50


# -->   # COUNT:-  "name.count(substring)"
p1 = "Dharmil panchal Dharmil"
print(p1.count("Dharmil"))
# Counts occurrences of substring


# -->   # ENDSWITH:- "name.endswith(substring)"
print(p1.endswith("Dharmil"))  # True

print(p1.endswith("il", 0, 7))
print(p1.endswith("al", 4, 15))
# Check if substring occurs at end in given slice


# -->   # STARTSWITH:- "name.startswith(substring)"
print(p1.startswith("Dh"))        # True
print(p1.startswith("m", 4, 15))  # False (4th char is 'm'?)


# -->   # FIND:- "name.find(substring)"
p2 = "My name is Dharmil,This is an example of find"
print(p2.find("is"))
# Returns first index of substring, or -1 if not found

print(p2.find("ishh"))
# -1 since substring doesn't exist


# --> IN / NOT IN operators return boolean
print("D" in ab)        # True
print("X" in ab)        # False
print("d" not in ab)    # True


# -->   # INDEX:- "name.index(substring)"
# NOTE:
# `index()` is similar to `find()` but raises an error if substring not found

# print(p2.index("ishh"))  # Would raise ValueError


# -->   # ISALNUM:- "name.isalnum()"
# Returns True if all characters are alphanumeric (A-Z, a-z, 0-9), no spaces
p3 = "MyNameIsDharmil123456"
p4 = "My Name Is Dharmil 122"

print(p3.isalnum())  # True
print(p4.isalnum())  # False


# -->   # ISALPHA:- "name.isalpha()"
# Returns True if all characters are alphabetic, no digits or spaces
print(p3.isalpha())
print("Python".isalpha())


# -->   # ISLOWER:- "name.islower()"
# True if all characters are lowercase
p5 = "my name is dharmil"
print(p5.islower())
print(p4.islower())


# -->   # ISUPPER:- "name.isupper()"
p51 = "MY NAME IS DHARMIL"
print(p51.isupper())


# -->   # ISPRINTABLE:- "name.isprintable()"
# True if all characters are printable (no tabs/newlines)
p6 = "My\t Name is Dharmil\n"
print(p6.isprintable())  # False due to \t and \n


# -->   # ISSPACE:- "name.isspace()"
# True if string contains only whitespace characters
p7 = "Python is easy to learn"
print(p7.isspace())  # False

p8 = " "
print(p8.isspace())  # True


# -->   # ISTITLE:- "name.istitle()"
# True if first letter of each word is capitalized
p4 = "My Name Is Dharmil"
print(p4.istitle())


# -->   # SWAPCASE:- "name.swapcase()"
# Converts uppercase to lowercase and vice versa
print(p4.swapcase())

words = {"aa","bb","cc"}
join = " ".join(words)
print(join)
