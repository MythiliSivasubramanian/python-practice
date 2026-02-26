"""
TUPLES — BASICS

A tuple is an immutable sequence of Python objects, once created, cannot be modified.

Key Properties:
• Ordered collection
• Immutable (cannot be modified after creation)
• Allows duplicate values
• Can store mixed data types
• Supports indexing and nesting

Topics Covered:

1. Creation Methods
2. Accessing Elements
3. Mixed Data Types & Immutability
4. Concatenation
5. Multiplication
  
"""

# CREATION METHODS

# Create a tuple with numbers 4, 5, 6 (including duplicate 6)

# Method 1 — Using parentheses ()

my_tuple = (4, 5, 6, 6)
print("\n\nTuple Creation Methods :\nMethod 1:Using parentheses () :\n", my_tuple,"\nDatatype :", type(my_tuple))

# Method 2 - Empty tuple
empty_tuple = ()
print("\nMethod 2: Empty Tuple:", empty_tuple, "\nDatatype :", type(empty_tuple))

# Method 3 - Single-element tuple (comma is required)
single_element_tuple = (5,)
print("\nMethod 3: Single-element Tuple:", single_element_tuple, "\nDatatype :", type(single_element_tuple))

# Method 4 — Omitting parentheses

# Commas automatically create a tuple

my_tup = 4, 5, 6
print("\n\nMethod 4 :\nOmitting parentheses :", my_tup,"\nDatatype :", type(my_tup))

# Method 5 — Conversion to tuple

# Convert any sequence or iterable into a tuple using tuple()
# 1. List → Tuple

mylist = [1, 2, 3, 4, 4]
list_tuple = tuple(mylist)
print("\n\nMethod 5 :\nList to Tuple:", list_tuple,"\nDatatype :", type(list_tuple))

# 2. String → Tuple
# Each character becomes an individual element

my_string = "Hello"
str_tup = tuple(my_string)
print("\nString to Tuple:", str_tup,"\nDatatype :", type(str_tup))

# Method 6 - Nested Tuples Creation

nested_tuples = (1, 2, 3), (1, 2, 3), (5, 6, 7)
print("\n\nMethod 6:\nNested Tuples:", nested_tuples, type(nested_tuples))


# ACCESSING ELEMENTS

"""
Elements in a tuple are accessed using indexing. Index starts from 0
"""
print("\n\n\nAccessing Elements")
# Access 2nd element (index = 1)

print("\nTuple : ",my_tuple, "\n2nd Element:", my_tuple[1])

# Access elements from nested tuple

print("\nNested tuple:", nested_tuples)

print("\nAccessing Outer elements: \n1st element:", nested_tuples[0],"\nAccessing 3rd element :", nested_tuples[2])

print("\nAccessing inner elements: 1st element 2nd value:", nested_tuples[0][1])

#  MIXED DATA TYPES & IMMUTABILITY

"""
Tuples can store mixed data types.
Even though tuples are immutable, mutable objects inside them can be modified.
"""

mixed_data_type_tuple = tuple(["food", [1, 2, 3], True])

print("\n\n\nMixed Data Type Tuple:" , mixed_data_type_tuple)

# mixed_data_type_tuple[0] = "hello"  # Error: tuples do not support item assignment

mixed_data_type_tuple[1].append(5) # List inside tuple is mutable — can modify in place

print("After modifying inner list:", mixed_data_type_tuple)

# TUPLE CONCATENATION

"""
Tuples can be concatenated using + operator. 
"""

tuple_1 = ([1, 2], "Hello", True, {1: "a", 2: "b"})
tuple_2 = ("Food", False, 2, 4, 9)

combined_tuple = tuple_1 + tuple_2

print("\nConcatenated Tuple:", combined_tuple)

#  TUPLE MULTIPLICATION

# Multiplying a tuple by an integer repeats its elements.

"""
Objects themselves are not copied. Only references are repeated.
"""

combined_tuple_2 = tuple_1 * 5
print("\n\n\nTuple Multiplication:", combined_tuple_2)

# Demonstrating reference behavior

# Modifying inner mutable object affects all repeated copies

combined_tuple_2[0].append(99)
print("\n\nAfter modifying inner list reference:", combined_tuple_2)