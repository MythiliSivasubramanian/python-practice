my_dict["name"] = "Micky"
my_dict.update(age=22, language="English, German")

# Accessing the elements in the dictionary

# Method 1: Using []
print(f"\nAccess name using [] : {my_dict['name']}")

# Method 2: Using get() (SAFE)
print(f"Access age using get() : {my_dict.get('age')}")
print(f"Access missing key safely : {my_dict.get('salary', 'Not Found')}")
