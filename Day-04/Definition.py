'''
--->>   Imagine if you have to print 1 to 15 in your program for 15 times,
        It will be too Lengthy, and in case after writing this code and now you 
        have to remove '14' from 1 to 15 from all 15 times;

--->>   You can do this efficiently by using ''function''.

--->>   Making function for sum, adding, avg, total, multiplication, etc...
        so it is easy to update any of this using function.

--->>   A function is a block of code that performs a specific task whenever it is called.
        In bigger programs, where we have large amounts of code, it is advisable to create
        or use existing functions that make the program flow organized and neat.

        1. Built-in functions 
            min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
        2. User-defined functions
            "Use 'def' and create function by our choice name."
'''

# -------------------- Without using functions --------------------
a = 10
b = 5
calculation = (a + b) / (a - b) * a
print(calculation)
if a > b:
    print(a, "is large")
else:
    print(b, "is large")

c = 15
d = 12
calculation1 = (c + d) / (c - d) * c
print(calculation1)
if c > d:
    print(c, "is large")
else:
    print(d, "is large")

e = 20
f = 17
print(calculation1)
if c > d:
    print(e, "is large")
else:
    print(f, "is large")

# But imagine this calculation is 10 lines long — you can't write this every time.
# You also can't write the "largest number" finding code every time.

# -------------------- Using functions --------------------
# Syntax: def name(arguments):

print("\n\n          USING FUNCTION   ✅  👀👀        \n\n")

def calculation(a, b):           # Define Function 1
    cal = (a + b) / (a - b) * a
    print("ANSWER:-- ", cal)

def large(a, b):                 # Define Function 2
    if a > b:
        print(a, "is large")
    else:
        print(b, "is large")

# Calling functions
a = 10
b = 5
calculation(a, b)
large(a, b)

c = 15
d = 12
calculation(c, d)
large(c, d)

e = 20
f = 17
calculation(e, f)
large(e, f)

'''
----->>>> Here you can see we created exactly same 3 examples but:
          - First 3 examples took 24 lines of code
          - Last 3 examples took 20 lines
          Remember: we only took 3 examples. 
          In a large program, functions are extremely helpful.
'''

# -------------------- Placeholder function --------------------
def large(a, b):
    pass
# pass means you will write the body of function later.

'''
--->>> Imagine you are making some very big project 🥸,
       then you can just declare ✅ ("NOT DEFINE ❌") 
       a function and tell your partner to build the body 😎.
       You can keep using this function while your partner writes it.

--->>> This is the actual use of function to work on large projects
       separately and then combine them later.
'''

# -------------------- More examples --------------------
def name(fname, lname):
    print("Hello, My name is", fname, lname)

name("Dharmil", "Panchal")


def square(num):
    return num * num

print("Square of 4 is:", square(4))


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print("Multiply 4 and 6:", multiply(4, 6))


# NOTE: We will learn recursion later in depth, this is just basic!
def factorial(n):
    """Returns factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))
