"""
Python Set Operations
- Union
- Intersection
- Difference
- Symmetric difference

What is expected:
- Understand mathematical set operations
- Learn multiple ways to perform the same operation
"""

A = {1, 2, 3}
B = {3, 4, 5}

#Union
print("Union using | :", A | B)
print("Union using union():", A.union(B))


#  Intersection
print("Intersection:", A & B)


#Difference
print("A - B:", A - B)
print("B - A:", B - A)


# Symmetric Difference
print("Symmetric Difference:", A ^ B)
