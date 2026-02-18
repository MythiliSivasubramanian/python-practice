"""Demonstrating all basic dictionary operations in Python.
- Two ways of creating dictionaries,
- Multiple methods to add new Key- Value pairs, 
- Two ways of updating exsisting values in dictionary,
- Multiple ways to access the exsisting values,
- Multiple ways to delete keys from a dictionary
"""

# Creating a dictionary with sample keys and values

# Method 1 : Creating dictionary using {}
profile = {
    "username": "coder123",
    "language": "Python"
}

# Method 2 : using dict() constructor
profile_2 = dict(username = "Jack",language = "c")

# Adding elements to a dictionary

# Method 1: using []
profile["experience"] = "Beginner"
# New key is added, when key 'experience' is not found

# Method 2: Using update(). helpful in updating multiple keys at once
profile.update({"country":"Italy","remarks":"new_user"})

# Method 3: using update() with keyword arguments
profile.update(age = 22)

# Method 4:  Using setdefault() Adds only, if key is new, will not overwrite keys if already found
profile.setdefault("timezone","CET")
profile.setdefault("language","phython 3") # Will not overwrite


# Update exsisting values in a dictionary
# Method 1: using []
profile["language"] = "Python 3"

# Method 2: using update(), also overwrites if key found
profile.update(experience = "Intermediate")

# Accessing dictionary values
# Method 1: using [], raises error if key is not found
print(f"\nUsername : {profile['username']}")

# Method 2 : Using get() returns none or default if key not found
print(f"\nAge is : {profile.get('age')},Land is : {profile.get('land','Not Found')}")


# Delete elements from Dictionary

# Method 1 : using del. Raises error if key not found
del profile["username"]

# Method 2 : using pop(). returns default value if key not found
profile.pop("currency",None)

# Method 3: using popitem() removes the last added paid
profile.popitem()

# Method 4: .clear() removes or clears all elements
print("\n Profile_2 dict is : ",profile_2)
profile_2.clear()
print("\n Profile_2 dict is : ",profile_2)

print(f"\nUpdated profile dictionary is : \n{profile}")
