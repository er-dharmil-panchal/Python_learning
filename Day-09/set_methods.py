#==========================================================================================================
#==========================================================================================================
#------->>>>>>>                                Set Methods                            <<<<<<---------
#==========================================================================================================
#==========================================================================================================

s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 6}

# 👉 union(): Returns a new set containing all unique items from both sets
print(s1.union(s2))    # {1, 2, 3, 4, 5, 6}

# 👉 update(): Adds items from another set into the current set
print(s1.update(s2))   # Output: None (because it modifies in place)
print(s1)              # {1, 2, 3, 4, 5, 6}

# 👉 intersection(): Returns a new set with only the common items
print("s1 =", s1, "\ns2 =", s2)
print(s1.intersection(s2))  # {1, 2}
print(s1)                   # s1 is unchanged

# 👉 intersection_update(): Keeps only common items in the set (modifies in place)
print(s1.intersection_update(s2))  # Output: None
print(s1)                          # {1, 2}


# 👉 symmetric_difference(): (A ∪ B) - (A ∩ B)
# basically gives only items that are not similar to both the sets
s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 6}

print(s1.symmetric_difference(s2))     # {3, 4, 5, 6}
print(s1)                              # s1 remains unchanged

# 👉 symmetric_difference_update(): same but it will change s1
print(s1.symmetric_difference_update(s2))   # None
print(s1)        # now s1 is {3,4,5,6}


# 👉 difference() and difference_update(): A - B
# prints only items that are present in the original set but not in the other set
print(s1.difference(s2))        # {3,4}
print(s1.difference_update(s2))
print(s1)                       # s1 is now {3,4}



#==========================================================================================================
#------->>>>>>>                      Manipulation Methods for Sets                    <<<<<<---------
#==========================================================================================================

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {7, 8, 9, 0}

# 👉 isdisjoint(): checks if items of one set are NOT present in another
print(s1.isdisjoint(s2))        # False
print(s1.isdisjoint(s3))        # True

# 👉 issuperset(): checks if all items of a set are present in the original set
s4 = {1, 2}
print(s1.issuperset(s2))        # False
print(s1.issuperset(s4))        # True

# 👉 issubset(): checks if all items of original set are present in another set
print(s4.issubset(s1))          # True
# NOTE: s4 is subset of s1, and s1 is superset of s4


# 👉 add(): add single item to the set
s4.add("India")
print(s4)

# 👉 update(): add multiple items (from iterable)
s1.update(s4)
print(s1)

# 👉 remove()/discard(): remove item from set
s1.remove(1)
s1.discard(2)
print(s1)
# NOTE: remove() raises error if item not present, discard() does not
# s1.remove(66)  # KeyError: 66
s1.discard(66)


# 👉 pop(): removes a random element (since sets are unordered)
print(s1.pop())
print(s1)

# 👉 del: deletes the entire set
del s1
# print(s1)   # NameError: name 's1' is not defined

# 👉 clear(): empties the set (keeps set object but removes all elements)
s2.clear()
print(s2)

# 👉 in keyword: check presence of item in set
print(7 in s3)
