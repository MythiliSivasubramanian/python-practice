"""
Nested dictionary operations: 
- Creation
- Modifying/updating values in inner dictionary
- Updating values in outer dictionary
- Adding new Key value pair in inner dictionary
- Updating multiple values at once using update()
"""

# Creating a nested dictionary 
student = {"name": "Rose", "marks": {"math": 90, "cs": 95}}
print(f"\nNested Dictionary : {student}\n")


# Updating values in inner dictionary
# Updating math marks from 90 → 98 (nested dictionary)
student["marks"]["math"] = 98
print(
    "\nUpdating math marks from 90 → 98 (nested dictionary):"
    "\nstudent['marks']['math'] = 98"
)
print(student)


# Updating value in outer dictionary
# Updating the value of key 'name' in outer dictionary
student["name"] = "Rose Sharma"
print(
    "\nUpdating the value of key 'name' in outer dictionary:"
    "\nstudent['name'] = 'Rose Sharma'"
)
print(student)


# Adding a new Key Value pair in inner dictionary
# Adding physics marks
student["marks"]["physics"] = 88
print(
    "\nAdding 'physics': 88 inside 'marks' using direct assignment:"
    "\nstudent['marks']['physics'] = 88"
)
print(student)


# Updating multiplr values in inner dictionary using update()
# Modifying "cs" to 99 and "physics" to 92
student["marks"].update(cs=99, physics=92)
print("\nAfter modfifying cs and physics marks : ",student)
