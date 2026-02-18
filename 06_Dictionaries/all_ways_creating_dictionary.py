"""
Python Dictionary Creation:
Multiple ways to create dictionaries in Python:
- Empty dictionaries using {} and dict()
- With initial values using {} and dict()
- From pairs (list of tuples)
- Using dictionary comprehension
"""


import sys
# Method 1: Creating an empty dictionary using {}
dict_1 = {}
print(f"dict_1 : {dict_1} | Type: {type(dict_1)} | Memory: {sys.getsizeof(dict_1)} bytes")

# Method 2: Creating an empty dictionary using dict()
dict_2 = dict()
print(f"dict_2 : {dict_2} | Type: {type(dict_2)} | Memory: {sys.getsizeof(dict_2)} bytes")

# Method 3: Creating dictionary with initial values
dict_3 = {"name": "Anna", "age": 25}
print(f"dict_3 : {dict_3} | Memory: {sys.getsizeof(dict_3)} bytes")

# Method 4: Using dict() with keyword arguments
dict_4 = dict(city="Berlin", country="Germany")
print(f"dict_4 : {dict_4}")

# Method 5: Creating dictionary from pairs
pairs = [("a", 1), ("b", 2)]
dict_5 = dict(pairs)
print(f"dict_5 : {dict_5}")

# Method 6: Dictionary comprehension
dict_6 = {x: x*x for x in range(5)}
print(f"dict_6 : {dict_6}")
