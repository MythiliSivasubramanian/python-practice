""" 
Demostrating basic dictionary operations in Python:
- Creating a Dictionary
-Adding and updating key Value pairs
- Accessing values using [] and ()
-Handling missing keys safely
"""

# Creating an empty dictionary
my_dict = {}

# Adding a Key and a value to the dictionary
my_dict["name"] = "Micky"

# Adding multiple keys and values using update()
my_dict.update(age=22, language="English, German")

print("\nUpdated Dictionary : ",my_dict)
# Accessing the elements in the dictionary

# Method 1: Using []
print(f"\nAccessing the value of key 'name' using [] : {my_dict['name']}")

# Method 2: Using get() (SAFE : returns none or deafult if key is missing)
print(f"\nAccessing the value of key 'age' using get() : {my_dict.get('age')}")
print(f"\nAccessing a missing key 'salary' safely : {my_dict.get('salary', 'Not Found')}")
