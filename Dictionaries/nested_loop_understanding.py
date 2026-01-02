"""
Nested Loops with Nested Dictionaries
"""

students = {
    "Alice": {"math": 85, "science": 90},
    "Bob": {"math": 70, "science": 60}
}

for name, inner_dict in students.items():
    print("\nStudent:", name)
    print("Subjects and Scores:")

    for subject, score in inner_dict.items():
        print(subject, score)
