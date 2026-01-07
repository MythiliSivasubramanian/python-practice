"""
Python Set Operations
- Union
- Intersection
- Difference
- Symmetric difference

What is expected:
<<<<<<< HEAD
- Understanding mathematical set operations
- Learning multiple ways to perform the same operation
=======
- Understand mathematical set operations
- Learn multiple ways to perform the same operation
>>>>>>> 276e3cb (Merge commit 'd986fde89a475ec9974c4205f4b8054130be024e')
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
