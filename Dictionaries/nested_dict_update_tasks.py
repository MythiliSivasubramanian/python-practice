student = {"name": "Rose", "marks": {"math": 90, "cs": 95}}
print(f"\nNested Dictionary : {student}\n")

# Updating math marks from 90 → 98 (nested dictionary)
student["marks"]["math"] = 98
print(
    "\nUpdating math marks from 90 → 98 (nested dictionary):"
    "\nstudent['marks']['math'] = 98"
)
print(student)

# Updating the value of key 'name' in outer dictionary
student["name"] = "Rose Sharma"
print(
    "\nUpdating the value of key 'name' in outer dictionary:"
    "\nstudent['name'] = 'Rose Sharma'"
)
print(student)

# Adding a new key-value pair inside inner dictionary
student["marks"]["physics"] = 88
print(
    "\nAdding 'physics': 88 inside 'marks' using direct assignment:"
    "\nstudent['marks']['physics'] = 88"
)
print(student)

# Updating multiple keys inside "marks" using .update() updating "cs" to 99 and "physics" to 92
student["marks"].update(cs=99, physics=92)
print(student)

# Adding the inner dictionary key 'address' - 'city' : 'Berlin', 'country' : 'germany'
# Method 1 : Create the inner dictionary first and then add
student["address"] = {}
student["address"]["city"] = "berlin"
student["address"]["country"] = "germany"
print("\nMethod 1: \nAdding the inner dictionary key 'address' - 'city' : 'Berlin', 'country' : 'germany' : \nstudent['address'] = {}\nstudent['address']['city'] = 'berlin'\nstudent['address']['country'] = 'germany' : \n",student)

# Method 2:
student["Address"] = {"stadt":"München","Land" : "Deutschland"}
print("\nMethod 2: \nAdding the inner dictionary key 'Address' - 'stadt' : 'München', 'Land' : 'Deutschland' : \nstudent['Address'] = {'stadt':'München','Land' : 'Deutschland'} : \n",student)

# Method 1: using = : Updating 'city' inside 'address' from 'berlin' to 'Hamburg'
student["address"]["city"] = "Hamburg"
print("\nUpdating 'city' inside 'address' from 'berlin' to 'Hamburg': \nMethod 1: using = : \nstudent['address']['city'] = 'Hamburg' \n",student)


# Method 2: using update() Updating 'stadt' inside 'address' from 'München' to 'stuttgart'
student["Address"].update(stadt = "stuttgart")
print("\n\nMethod 2:\nusing update()\nUpdating 'stadt' inside 'address' from 'München' to 'stuttgart' : \n",student)


# Updating 'pincode' if 'address' exsists. using .get()
if student.get("address") is not None:
    student["address"]["pincode"] = 12345
    
print("\nUpdating 'pincode' if 'address' exsists. using .get() : \nsteps: if student.get('address') is not None:\n\t student[address][pincode] = 12345 \n",student)

# Removing 'physics' key safely using .pop()
removed_value = student["marks"].pop("physics", None)
print("\nRemoving 'physics' key from 'marks' using .pop() if it exists")
print("Removed value:", removed_value)
print("Updated student dictionary:\n", student)

# Clearing the inner dictionary 'Address' using .clear()
student["Address"].clear()
print("\nClearing the inner dictionary 'Address' using .clear()")
print("Updated student dictionary:\n", student)
