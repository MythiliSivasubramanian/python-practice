"""
File        : student_marks_aggregator.py
Topic       : Python Dictionaries
Practice    : Aggregation & Grouping Logic

Task:
- Calculate total marks per student
- Count subjects per student
- Compute average marks
- Identify top-performing student

Concepts:
Dictionary aggregation, frequency counting,
average calculation, manual ranking logic
"""


"""
Task: “Subject Marks Aggregator”
You’re given student subject marks like this: with Same student and same subject appears multiple times but marks varies
records = [
            ("Anu", "Math", 78),
            ("Bala", "Math", 45),
            ("Anu", "Science", 88),
            ("Cathy", "Math", 92),
            ("Bala", "Science", 55),
            ("Anu", "Math", 81)]

Task 1 — Create Total Marks per Student
Task 2 - Count Subjects per Student
Task 3 - Average Marks per Student and round tp 2 decimals
Task 4 — Find student with highest average marks. wi9thout max()
"""

# Predefined students marks
records = [
            ("Anu", "Math", 78),
            ("Bala", "Math", 45),
            ("Anu", "Science", 88),
            ("Cathy", "Math", 92),
            ("Bala", "Science", 55),
            ("Anu", "Math", 81)]


# Task 1 — Create Total Marks per Student
students_total_marks = {} # Empty dict to store students aggregated marks
for name, subject, mark in records:
    if name in students_total_marks:
        students_total_marks[name] += mark
    else:
        students_total_marks[name] = mark
print("\n\nStidents total marks :\n", students_total_marks)


# Task 2 - Count Subjects per Student

students_subjects_count = {}
for name, subject, mark in records:
    if name in students_subjects_count:
        students_subjects_count[name] += 1
    else:
        students_subjects_count[name] = 1
    
print("\n\nStudents Subjects count : \n", students_subjects_count)


# Task 3 — Average Marks per Student
# Total marks per student / no of subjects

students_average_mark = {}

for name in students_total_marks:
    total = students_total_marks[name]
    count = students_subjects_count[name]
    
    students_average_mark[name] = round(total /count, 2)
    
print("\n\nStudents Average Marks :\n", students_average_mark)

# Task 4 — Find student with highest average marks. without max()
top_student = None
highest_marks_avg = 0

for name, avg_mark in students_average_mark.items():
    if avg_mark > highest_marks_avg:
        highest_marks_avg = avg_mark
        top_student = name
print("\n\nTop Student :",  top_student,"\tHighest_average_mark :", highest_marks_avg)