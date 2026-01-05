my_dict["name"] = "Micky"

# Adding multiple keys and values using update()
my_dict.update(age=22, language="English, German")

print("\nUpdated Dictionary : ",my_dict)
# Accessing the elements in the dictionary

# Method 1: Using []
print(f"\nAccessing the value of key 'name' using [] : {my_dict['name']}")

# Method 2: Using get() (SAFE)
print(f"Access age using get() : {my_dict.get('age')}")
print(f"Access missing key safely : {my_dict.get('salary', 'Not Found')}")
