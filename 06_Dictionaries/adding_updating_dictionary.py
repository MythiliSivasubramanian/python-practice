"""
Different ways to add and update dictionary elements in Python and 
checking the memory usage of it using sys.getsizeof()
"""

import sys

# Creating a empty dictionary using {}
my_dict = {}
print(f"\nInitial my_dict : {my_dict} | Memory: {sys.getsizeof(my_dict)}\n")
# sys.getsizeof() returns the memory size of the object in bytes

# Method 1: Adding a key - value in dictionary
my_dict["name"] = "Anna Maria"
print(f"\nAfter adding a key value pair :\n {my_dict} | Memory: {sys.getsizeof(my_dict)}")

# Method 2: Updating an existing key
my_dict["name"] = "Micky"
print(f"\nAfter updating the key 'name' :\n {my_dict}  | Memory: {sys.getsizeof(my_dict)}")

# Method 3: update() method (can update single/ multiple keys at once)
my_dict.update(age=22, language="English, German")
print(f"\nAfter updating multiple keys,dictionary is : \n{my_dict} | Memory: {sys.getsizeof(my_dict)}")

# Method 4: setdefault() (adds only if key missing)
my_dict.setdefault("country", "Germany")
my_dict.setdefault("age", 30)  # will not overwrite exsistimg values
print(f"\nAfter setdefault() : \n{my_dict} |Memory: {sys.getsizeof(my_dict)}")