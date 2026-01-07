""" Create a set with at least 5 numbers
- Print the set
- Add one new number
- Remove one number
Goal: Understand uniqueness and basic methods
"""
# Creating a Set with 5 numbers
numbers_set = {1, 2, 3, 4, 5}
print("Printing the set:", numbers_set)

# Adding one number
numbers_set.add(8)
print("After adding 8:", numbers_set)

# Removing a number safely
numbers_set.discard(8)
print("After discarding 8:", numbers_set)

# Removing a number (element must exist, else raises error)
numbers_set.remove(5)
print("After removing 5:", numbers_set)
