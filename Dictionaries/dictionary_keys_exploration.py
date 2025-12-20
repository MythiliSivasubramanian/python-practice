"""A Python script to explore how dictionary keys behave in different scenarios
and to demonstrate dynamic vs static keys"""

# Creating a dictionary from variables (dynamic keys)

key_1 = "one"
key_2 = "two"
key_3 = "three"
dict_1 = {key_1: 1, key_2: 2, key_3: 3}  # dictionary keys come from variable values
print(f"\nDictionary created from variables: {dict_1}\n")

# Changing the variables after dictionary creation
print(f"Before changing variables: key_1={key_1}, key_2={key_2}, key_3={key_3}")
key_1 = "first"
key_2 = "second"
key_3 = "third"
print(f"After changing variables: key_1={key_1}, key_2={key_2}, key_3={key_3}")
print(f"Dictionary does not change after variable update: {dict_1}\n")


# Static keys using keyword arguments
dict_2 = dict(a=10, b=20, c=30)
print(f"Dictionary using dict() with keyword arguments: {dict_2}\n")

# Attempting invalid keyword (uncommenting will cause SyntaxError)
# dict_3 = dict(first-name="Anna")  #  invalid identifier
print("'first-name' is an invalid identifier for dict() keyword argument\n")


# Keys with different immutable types
dict_4 = {(1, 2): "tuple with immutable objects", 1: "integer", "Hello": "string"}
print(f"Dictionary with different immutable key types: {dict_4}\n")

# Immutable key error demonstration
try:
    dict_5 = {[1, 2]: "list"}  # Lists are mutable → cannot be dictionary keys
except TypeError:
    print("Keys are immutable, cannot use list as a dictionary key\n")

# Dynamic keys using variable values
dynamic_key = "dynamic"  # variable holding a string
dict_6 = {dynamic_key: 100}  # dictionary key is the value of the variable
print(f"Dictionary with dynamic key from variable value: {dict_6}")
