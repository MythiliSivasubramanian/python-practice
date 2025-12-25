
# Creating a nested dictionary
student = {"name": "Rose","Age": 20, "marks": {"math": 98, "cs": 99},"address": {"city": "Hamburg", "country": "Germany"}}

# student_copy is the shallow copy of the student dictionay. inner dictionary is shared.
student_copy = student.copy()


print("Original nested dictionary:\n", student)
student_shallow = student.copy()
print("\nShallow copy of student created:\n", student_shallow)

# Modify outer key
student["Age"] = 21
print("\nAfter modifying outer key 'Age':")
print("Original:", student)
print("Shallow copy:", student_shallow)

# Modify inner key
student["marks"]["math"] = 100
print("\nAfter modifying inner key 'marks[math]':")
print("Original:", student)
print("Shallow copy:", student_shallow)
