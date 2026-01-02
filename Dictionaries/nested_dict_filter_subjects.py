"""
Filter Nested Dictionary. Keepingh only subjects where score >= 80
"""

students = { "Alice": {"math": 85, "science": 90},"Bob": {"math": 70, "science": 60}}

# Filter subjects with score >= 80
top_scores = {student: {subject: score for subject, score in subjects.items() if score >= 80} for student, subjects in students.items()}

print("Subjects with score >= 80: ",top_scores)
