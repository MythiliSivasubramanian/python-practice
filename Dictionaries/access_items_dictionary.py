"""
Dictionary:
- Adding key-value pairs to a dictionary
- Updating existing keys
- Accessing dictionary elements safely using [] and get()
"""
# Creating an empty dictionary
my_dict = {}

# Adding a key-Value pairs using [] and update()
# update() is used for updating multiple keys at once
my_dict["name"] = "Micky"
my_dict.update(age=22, language="English, German")

# Accessing the elements in the dictionary

# Method 1: Using []
print(f"\nAccess name using [] : {my_dict['name']}")

# Method 2: Using get() (SAFE : returns None or default if key missing)
print(f"Access age using get() : {my_dict.get('age')}")
print(f"Access missing key safely : {my_dict.get('salary', 'Not Found')}")
