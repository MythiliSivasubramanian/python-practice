"""A Python script that demonstrates all three ways to create dictionaries 
and shows how dictionary keys work with variables, keyword syntax, and iterables."""

# Creating a dictionary from variables (dynamic keys)

# key1 and value1 are variables
key1 = "fruit"
value1 = "apple"

# Creating dictionary using the value of variables as key and value
dictionary_1 = {key1: value1} 
print(f"\nThe Dictionary_1 is: {dictionary_1}")

# Change the variables after dictionary creation
# The dictionary key/value remains unchanged because the dictionary stores the **current value of the variable** at creation
key1 = "colors"
value1 = "Red"
print(f"\nChange in variable after dictionary creation does NOT affect Dictionary_1:\nDictionary_1 is: {dictionary_1}")

# Creating a dictionary using dict() with keyword arguments (static keys)
# Keys are based on **keyword argument names**, not variable names
static_dictionary = dict(color="Red", size=10)  
# 'color' and 'size' are always strings and cannot be dynamically determined from variables
print(f"\nDictionary using dict() with keyword arguments: {static_dictionary}")


# Creating a dictionary from an iterable of key-value pairs (dynamic keys)
pairs = [("x", 100), ("y", 200)]  # List of tuples
dynamic_dictionary = dict(pairs)  # Each tuple: (key, value)
print(f"\nDictionary created from iterable of pairs: {dynamic_dictionary}")
# Dynamic because keys/values come from the iterable; changing the iterable later won't affect the dictionary


# Demonstrating different immutable key types
dict_2 = {(1, 2): "tuple", 99: "integer", "Hello": "string"}
print(f"\nDictionary with different immutable key types: {dict_2.items()}")
# Keys are all immutable: tuple, integer, string


# Attempting to use a mutable object as a key (raises TypeError)

try:
    dict_3 = {[1, 2]: "list"}  # Lists are mutable , cannot be dictionary keys
except TypeError:
    print(f"\nKeys are immutable, cannot use list as a key")
