"""
Nested Dictionary Comprehension
Checking if Pass / Fail in a subject.  Pass if score >= 60, otherwise Fail
"""

# Creating a nested ictionary with students names and marks in respective subjects
students = {"Alice": {"math": 85, "science": 90},"Bob": {"math": 70, "science": 60}}

# Nested dictionary comprehension with condition
result = {student: {subject: "Pass" if score >= 60 else "Fail" for subject, score in subjects.items()} for student, subjects in students.items()}

print("Pass / Fail using dictionary comprehension : \n")
print(result)
