"""
Tuples – Indexing & Slicing 

Tuple indexing and slicing 
using positive, negative and step-based slicing.
"""
# Sample tuple
t = (10, 20, 30, 40, 50, 60)
print("\n\nOriginal Tuple:", t)

# 1. Basic Indexing

print("\nBasic Indexing: \n\nIndex 0 :", t[0])
print("Index 2 :", t[2])
print("Last index :", t[-1])
print("Second last :", t[-2])

# 2. Basic Slicing  [start : end] end is excluded

print("\n\nBasic Slicing\n\nt[0:3]  :", t[0:3])
print("t[1:4]  :", t[1:4])
print("t[:3]   :", t[:3])
print("t[3:]   :", t[3:])
print("t[:]    :", t[:])     # Full copy


# 3. Negative Index Slicing

print("\n\nNegative Index Slicing\n\nt[-4:-1] :", t[-4:-1])
print("t[-3:]   :", t[-3:])
print("t[:-2]   :", t[:-2])

# 4. Step Slicing  [start : end : step]

print("\n\nStep Slicing\n\nt[0:6:2] :", t[0:6:2])   # Every 2nd element
print("t[::2]   :", t[::2])     # Skip 1
print("t[1::2]  :", t[1::2])    # Start from index 1


# 5. Reverse Slicing

print("\n\nReverse Slicing\n\nt[::-1]      :", t[::-1])     # Full reverse
print("t[4:1:-1]   :", t[4:1:-1])
print("t[::-2]     :", t[::-2])     # Reverse step 2


# Edge Cases

print("\n\nEdge Cases\n\nt[10:]  :", t[10:])     # Out of range → empty
print("t[:10]  :", t[:10])     # Safe → full tuple
print("t[3:3]  :", t[3:3])     # Empty slice

# 7. Membership & Length

print("\n\nMembership & Length\n\nLength :", len(t))
print("Is 30 present?", 30 in t)
print("Is 99 present?", 99 in t)

# 8. Index Error Demonstration

try:
    print("\n\nIndex Error Demonstration ",t[100])
except IndexError as e:
    print("\n\nIndexError:", e,"\n\n")