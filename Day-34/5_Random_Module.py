"""
📌 NumPy – Step 5 (Random Module)

This file covers:
    - Random Integers using np.random.randint()
    - Random Floats using np.random.rand(), np.random.random(), np.random.uniform()
    - Random Choice using np.random.choice() (with/without replacement, weighted probabilities)
    - Random Distributions using np.random.randn(), np.random.normal()
    - Shuffling & Permutations using np.random.shuffle() & np.random.permutation()
    - Seeding using np.random.seed() for reproducibility

📝 Summary:
    - NumPy random module is essential for ML, simulations, testing, and games.
    - randint() → generate random integers
    - rand(), random(), uniform() → generate random floats
    - choice() → pick elements randomly (with/without replacement, probabilities)
    - randn(), normal() → normal distributions (standard & custom)
    - shuffle() → modifies array in-place, permutation() → returns shuffled copy
    - seed() → ensures reproducible random numbers
"""

# =============== Random Integers (randint) =================

import numpy as np
import sns

# randint(low, high, size)
arr = np.random.randint(1, 10)
print(arr)
# Generates integers between 1 (inclusive) and 10 (exclusive).

arr = np.random.randint(1, 10, 6)
print(arr)  # [3 3 1 5 3 8]

# =============== Random Float (rand, random, uniform) =================
# Always between 0 and 1.
print(np.random.rand(5))  # [0.30853463 0.41916065 0.18578821 0.50931967 0.25214749]
print(np.random.rand(2, 2))  # [[0.17120549 0.23821284]
# [0.6365208  0.11293997]]

print(np.random.random(2))  # [0.72007884 0.2330762 ]
# same thing, another syntax

print(np.random.uniform(5, 10, size=5))  # [8.94929365 8.54967314 5.98505555 9.7758733  7.85206774]
# 5 floats between 5 and 10


# =============== Random Choice =================
# This is used to pick elements randomly from an array (or a range of numbers). Very handy in sampling, simulations, or games.

arr = np.array([10, 20, 30, 40, 50])
print(np.random.choice(arr))  # 20
print(np.random.choice(arr, 2))  # [40 20]

# 👉🏻 With replacement
print(np.random.choice(arr, 5, replace=True))  # elements may duplicate -> [30 30 10 10 40]

# 👉🏻 Without replacement
print(np.random.choice(arr, 5, replace=False))  # elements will not duplicate -> [20 40 30 50 10]
# print(np.random.choice(arr, 10, replace=False))  # ValueError: Cannot take a larger sample than population when 'replace=False'

# 👉🏻 Weighted Probabilities

# probability distribution: 10->0.5, 20->0.1, 30->0.1, 40->0.1, 50->0.2
print(np.random.choice(arr, 5, p=[0.5, 0.1, 0.1, 0.1, 0.2]))  # sum must be 1
# [50 10 40 10 30] -> ( based on probability)
print(np.random.choice(arr, 5, p=(0.5, 0, 0, 0, 0.5)))
# [50 50 50 50 10]
print(np.random.choice(arr, 5, p=(0, 1, 0, 0, 0)))
# [20 20 20 20 20]

print(np.random.choice(10, 5))  # pick 5 numbers from 0–9

# =============== Random Distributions =================
# NumPy allows you to generate numbers that follow statistical distributions. This is key in ML, simulations, testing, etc.
# Mean = center of numbers
# Std = how “wide” the numbers are around the center

# 👉🏻 a) Standard Normal Distribution → np.random.randn()
# Standard normal = mean = 0, std (standard deviation) = 1.
# Numbers can be negative or positive; most cluster around 0.

print(np.random.randn(5))  # 5 numbers from standard normal

# 👉🏻 b) Custom Normal Distribution → np.random.normal()

print(np.random.normal(50, 10, 5))
# mean=50, std=10, size=5
# Most numbers hover around 50 (mean), spread depends on std (10 here).

# 👉🏻 Binomial Distribution
# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
# It has three parameters:
#       n - number of trials.
#       p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
#       size - The shape of the returned array.

print(np.random.binomial(n=1, p=0.5, size=10))

# Difference Between Normal and Binomial Distribution
# The main difference is that normal distribution is continuous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
# which we will see more in detail after learning matplotlib.

# =============== Shuffling & Permutations =================
# Randomly reordering elements of an array.

# a) Shuffle in-place → np.random.shuffle() :- Modifies arr itself.
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

# b) Return a shuffled copy → np.random.permutation()
arr2 = np.array([10, 20, 30, 40, 50])
shuffled = np.random.permutation(arr2)
print(shuffled)
print(arr2)  # original stays the same

# Difference: shuffle changes original array, permutation makes a new shuffled array.


# =============== Seeding – Reproducibility =================
# When you generate random numbers, computers don’t produce truly random numbers—they use a pseudo-random algorithm.
# That means it follows a formula to create numbers that “look random.”
# Every time you run your program without a seed, the numbers will be different.

# Problem Without a Seed
print(np.random.randint(1, 100, 5))
# 1st run :-    [65 49 86 95 14]
# 2nd run :-    [66 40 24 73 42]

# Solution -> Seed
# Seed is like giving the random generator a starting point.
# Same seed -> same sequence of random numbers every time.

np.random.seed(13)  # set the seed
print(np.random.randint(1, 100, 5))
# 1st run :-    [83 49 75 17 99]
# 2nd run :-    [83 49 75 17 99]
# 3rd run :-    [83 49 75 17 99]

np.random.seed(23)
print(np.random.randint(1, 100, 5))
# [84 41 74 55 32]

np.random.seed(13)
print(np.random.randint(1, 100, 5))
# [83 49 75 17 99] -> Again same ans

# Same seed = same random numbers

"""
📌 Why is Seeding Important?
    - Reproducibility in experiments:
        If you train an ML model and want to test results later, using a seed ensures your “random” data splits are exactly the same.
    - Debugging:
        Makes your program predictable. Without a seed, bugs could appear randomly.
    - Sharing results:
        Others can run your code and get the same random numbers, which is essential in research or competitions.
"""

# =============== Practice Task =================

# 1) Create 5 random integers between 10 and 50
print(np.random.randint(10, 50, 5))

# 2) Create 3 random floats between 0 and 1
print(np.random.random(3))

# 3) Pick 4 random elements from array [5,10,15,20,25] without replacement
print(np.random.choice(np.array([5, 10, 15, 20, 25]), 4, replace=False))

# 4) Generate 5 numbers from normal distribution with mean=0, std=1
print(np.random.randn(5))

# 5) Shuffle array [1,2,3,4,5,6]
arr = np.array([1, 2, 3, 4, 5, 6])
np.random.shuffle(arr)
print(arr)

# 6) Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
print(np.random.choice(np.array([3,5,7,9]),size=(3,5)))

# 7) Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1,  5 is set to be 0.3, 7 is set to be 0.6, 9 is set to be 0
print(np.random.choice(np.array([3,5,7,9]),size=(100), p=[0.1, 0.3, 0.6, 0]))

# 8) Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
print(np.random.choice(np.array([3,5,7,9]),size=(3,5), p=[0.1, 0.3, 0.6, 0]))

"""
📌 Quick Recap
    - randint() → random integers
    - rand(), random(), uniform() → random floats
    - choice() → pick elements randomly (with/without replacement, probabilities)
    - randn(), normal() → normal distributions
    - shuffle() & permutation() → randomize arrays
    - seed() → reproducibility
"""
