"""
Nested Dictionary:
- Creating a nested dictionary
- Updating exsisting values in nested dictionary
- Modifying values in outer dictionary
- Adding new key - value pairs in inner dictionary
"""

#  Creating a nested dictionary
student = {"name": "Rose", "marks": {"math": 90, "cs": 95}}
print(f"\nNested Dictionary : {student}\n")


# Updating values in nested dictionary
# Updating math marks from 90 → 98 (nested dictionary)
student["marks"]["math"] = 98
print(
    "\nUpdating math marks from 90 → 98 (nested dictionary):"
    "\nstudent['marks']['math'] = 98"
)
print(student)


# Updating values in outer dictionary
# Updating the value of key 'name' in outer dictionary
student["name"] = "Rose Sharma"
print(
    "\nUpdating the value of key 'name' in outer dictionary:"
    "\nstudent['name'] = 'Rose Sharma'"
)
print(student)



# Adding a new Key value pair in inner dictionary
# Adding a new key-value pair inside inner dictionary
student["marks"]["physics"] = 88
print(
    "\nAdding 'physics': 88 inside 'marks' using direct assignment:"
    "\nstudent['marks']['physics'] = 88"
)
print(student)


# Updating multiple keys in inner dict using .update()
# Updating multiple keys inside "marks" using .update() updating "cs" to 99 and "physics" to 92
student["marks"].update(cs=99, physics=92)
print(student)


# Adding a new inner dictionary
# Adding a new inner dictionary key 'address' - 'city' : 'Berlin', 'country' : 'Germany' 
# Method 1 : Create an empty inner dictionary first and then add keys
student["address"] = {}
student["address"]["city"] = "Berlin"
student["address"]["country"] = "Germany"
print("\nMethod 1: \nAdding the inner dictionary key 'address' - 'city' : 'Berlin', 'country' : 'Germany' : \nstudent['address'] = {}\nstudent['address']['city'] = 'Berlin'\nstudent['address']['country'] = 'Germany' : \n",student)


# Method 2: Adding inner dictionary directly
student["address"] = {"stadt":"München","Land" : "Deutschland"}
print("\nMethod 2: \nAdding the inner dictionary key 'address' - 'stadt' : 'München', 'Land' : 'Deutschland' : \nstudent['address'] = {'stadt':'München','Land' : 'Deutschland'} : \n",student)


# Updating inner dictionary values
# Method 1: using = : Updating 'city' inside 'address' from 'Berlin' to 'Hamburg'using assignment and []
student["address"]["city"] = "Hamburg"
print("\nUpdating 'city' inside 'address' from 'Berlin' to 'Hamburg': \nMethod 1: using = : \nstudent['address']['city'] = 'Hamburg' \n",student)


# Method 2: using update(): Updating 'stadt' inside 'address' from 'München' to 'stuttgart'
student["address"].update(stadt = "stuttgart")
print("\n\nMethod 2:\nusing update()\nUpdating 'stadt' inside 'address' from 'München' to 'stuttgart' : \n",student)



# Safe updating using .get()
# Add 'pincode' only if 'address' exists. using .get()
if student.get("address") is not None:
    student["address"]["pincode"] = 12345
    
print("\nAdding 'pincode' only if 'address' exists. using .get() : \nsteps: if student.get('address') is not None:\n\t student[address][pincode] = 12345 \n",student)


# Removing values from inner dictionary
# Removing key 'physics' safely using .pop()
removed_value = student["marks"].pop("physics", None)
print("\nRemoving 'physics' key from 'marks' using .pop() if it exists")
print("Removed value:", removed_value)
print("Updated student dictionary:\n", student)



# Clearing the inner dictionary 'address' using .clear()
student["address"].clear()
print("\nClearing the inner dictionary 'address' using .clear()")
print("Updated student dictionary:\n", student)
