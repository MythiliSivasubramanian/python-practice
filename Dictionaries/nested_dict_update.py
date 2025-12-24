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
