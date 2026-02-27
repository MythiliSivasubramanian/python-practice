"""
Tuples: Packing and Unpacking 

1. Basic unpacking
2. Unpacking using *
3. Unpacking in loops

"""


"""
Unpacking Tuples:

Number of variables should match number of elements OR use * to collect remaining elements.

Each tuple element is assigned to the variable at the same position on the left side.

If a variable is prefixed with *, it collects multiple values into a list.

"""

# Basic unpacking
t = (10, 20, 30) # Sample Tuple
print(f"\nOriginal tuple : {t}\n")
# Unpack values 10,20,30 to a,b,c
a, b, c = t
print(f"Unpacking values of tuple to a, b, c :\n"
      f"a is {a}\nb is {b}\nc is {c}\n")

# Using * to collect remaining values
t1 = (10, 20, 30, 40, 50)
a1, *b1, c1 = t1 # *b1 collects all middle values as a list [20,30,40]
print(f"\nOriginal tuple t1 : {t1}\n")
print(f"Unpacking values of tuple t1 to a1, b1, c1 using *b1:\n"
      f"a1 is {a1}\nb1 is {b1}\nc1 is {c1}\n")

# Using * at the beginning
t3 = (1, 2, 3, 4, 5)
*start, last = t3
print("\n\nUsing * at the beginning:")
print(f"\nOriginal tuple t3 : {t3}\n"
      f"unpacking the values of t3 as start and last :\n")
print("start:", start)
print("last:", last)

# Error when too many values to unpack
t2 = (10,100,100,10000)
print("\n\nError when mismatch between number of variables and number of tuple elements (not involving *)")
print(f"\nTuple T2 : {t2}\n"
      f"Unpacking values of T2 to a_1 and a_2 :\n")
try:
    a_1, a_2 = t2
    print(f"\na_1 : {a_1}\na_2 : {a_2}")
except ValueError as e:
    print(f"Error Message is : {e}\n")
    
# Unpacking in loops
pairs = [(1, 2), (3, 4), (5, 6)] # Sample list of tuples
print(f"\n\nUnpacking in Loops :\n"
      f"\npairs : {pairs}\n"
      f"unpacking as a and b\n")

for a,b in pairs:
    print(f"a is {a}\tb is {b}")