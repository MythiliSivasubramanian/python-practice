"""
Nested Dictionary Comprehension – Pass / Fail.  Pass if score >= 60
"""

students = {"Alice": {"math": 85, "science": 90},"Bob": {"math": 70, "science": 60}}

# Nested dictionary comprehension
result = {student: {subject: "Pass" if score >= 60 else "Fail" for subject, score in subjects.items()} for student, subjects in students.items()}

print("Pass / Fail using dictionary comprehension : \n")
print(result)
