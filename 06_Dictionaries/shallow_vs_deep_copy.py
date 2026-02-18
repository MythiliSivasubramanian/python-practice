"""
Shallow copy vs deep copy in nested dictionary:
Shallow copy:
- Outer dictionary is copied, inner dictionaries are shared.
- Changes to outer keys do not affect the shallow copy.
- Changes to inner keys affects the shallow copy, since inner dict is shared reference.+
Deep copy:
- Full independent copy
- changes in either outer or inner dictionary doesnt affect the copy
""" 

import copy

# Original nested dictionary
student = {"name": "Rose","Age": 20, "marks": {"math": 98, "cs": 99},"address": {"city": "Hamburg", "country": "Germany"}}

# Creating two copies
student_shallow = student.copy()  # Shallow copy
student_deep = copy.deepcopy(student) # Deep copy

print("\nOriginal nested dictionary :", student)
print("Shallow copy of student :", student_shallow)
print("Deep copy of student :", student_shallow)


# Modifying outer key 'age' in original nested dictionary
student["Age"] = 21
print("\nAfter modifying outer key 'Age' in Original dict : ")
print("Original : ", student)
print("Shallow copy : ", student_shallow)
print("Deep copy : ", student_deep)

# Modifying inner key 'math' from 'marks' in original dictionary
student["marks"]["math"] = 100
print("\nAfter modifying inner key 'marks[math]' in Original dictionary : ")
print("Original : ", student)
print("Shallow copy : ", student_shallow)
print("Deep copy : ", student_deep)

# Modifying inner key in deep copy
student_deep["marks"]["cs"] = 55
print("\nAfter modifying inner key 'marks[cs]' in deep copy : ")
print("Original : ", student)
print("Shallow copy : ", student_shallow)
print("Deep copy : ", student_deep)