# =========================================================
# Example 1: Simple Recursion (Print "Hii 1" to "Hii 5")
# =========================================================
# Recursion is to call function inside same function 

def print5(i):
    if (i > 5):                 # End condition
        return
    print(f"Hii {i}")
    i += 1
    return print5(i)

i = 1
print5(i)

# recursion requier a end conditon same like loops,
# building logic to use recursion at right position is help to improve problem solving.


# =========================================================
# Example 2: Factorial using Recursion
# =========================================================
# example : Factorical()

"""
factorial(5) = 5x4x3x2x1 = 120
which is alos = 5 * factorial(4) -> 4 * factorial(3)....

so factorial(n) is actuallu  = factorial(n-1) * n
so here we can see that for factorial we can use the same function to do the function 
"""

def factorial(n):
    if (n == 0 or n == 1):      # End condition
        return 1
    return n * factorial(n-1)

print("Factorical of 5 is = ", factorial(5))

"""
dry run : 
    factorial(5)        -> return 5 * factorial(4)
    factorial(4)        -> return 4 * factorial(3)
    factorial(3)        -> return 3 * factorial(2)
    factorial(2)        -> return 2 * factorial(1)
    factorial(1)        -> return 1

After reaching the end condition:
    factorial(1) returns 1 to factorial(2)
    factorial(2) returns (2*1 = 2) to factorial(3)
    factorial(3) returns (3*2 = 6) to factorial(4)
    factorial(4) returns (4*6 = 24) to factorial(5)
    factorial(5) returns (24*5 = 120) where function called.
"""


# =========================================================
# Example 3: Fibonacci using Recursion
# =========================================================
"""
Fibonacci :- 0 1 1 2 3 5 8 13 ...
fo = 0
f1 = 1
f2 = fo + f1

fn = fn-1 + fn-2
"""

def fibo(fo, f1, count):
    if (count > 10):            # End condition (print first 10 numbers)
        return
    print(fo, end=',')
    count += 1
    return fibo(f1, fo + f1, count)

print("\nFibonacci Series (First 10 terms):")
fo = 0
fi = 1
fibo(fo, fi, 1)
print()


# =========================================================
# Example 4: Sum of Digits of a Number
# =========================================================

def sumOfDigit(n):
    if(n == 0):
        return 0
    return (n%10) + sumOfDigit(n//10)

print(f"sum of digits of 12345 = {sumOfDigit(12345)}")


# =========================================================
# Example 5: Count Ways to Climb Stairs
# =========================================================
"""
Ways to climb stairs if allowed steps = 1 or 2
Base: ways(0) = 1
Recursive: ways(n) = ways(n-1) + ways(n-2)
"""
def ways(countOfStairs):
    if countOfStairs == 0:
        return 1
    if countOfStairs < 0:
        return 0
    return ways(countOfStairs-1) + ways(countOfStairs-2)

for i in range(3, 14):
    print(f"There are {ways(i)} ways to climb {i} stairs (1,2 steps)")

# NOTE: Recursive solutions grow very fast because each call 
#       spawns multiple sub-calls. For climbing stairs with {1,2,3} steps,
#       even a small input creates hundreds of recursive calls.
#       Example: ways(10) = 653, ways(11) = 1201 😮.
