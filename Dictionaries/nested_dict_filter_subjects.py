"""
Filtering a nested Dictionary,keeping only subjects where score >= 80. 
If scores are less than 80, print empty dictionary
"""

# Predefined nested dictionary with students name and thier marks in respective subjects
students = { "Alice": {"math": 85, "science": 90},"Bob": {"math": 70, "science": 60}}

# Filter subjects with score >= 80 using nested dict comprehension with condition
top_scores = {student: {subject: score for subject, score in subjects.items() if score >= 80} for student, subjects in students.items()}

print("Subjects with score >= 80: ",top_scores)
