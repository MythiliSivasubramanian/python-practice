"""
Practice: List Comprehension, zip, and enumerate

- Combine two lists using zip
- Add indexing with enumerate
- Build formatted strings using list comprehension and f-strings
"""


# Predefined lists
students = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 92, 78, 90]

# Combbining students name and thier scores using zip()

student_scores = list(zip(students,scores))
print(student_scores,"\n")


# Printing the names and scores of each student in more readable format

report = [f"{index}.{student} scored {score}"
          for index, (student, score) in enumerate(student_scores, start=1)]

print(report)
