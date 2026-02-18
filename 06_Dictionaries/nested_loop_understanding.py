"""
Nested Loops with Nested Dictionaries:
- Iterating over nested dictionary using nested loops
- Accessing outer dictionary keys
- Accessing inner dictionary keys and values
"""

# Creating nested dictionary with names and score of respective subjects
students = {
    "Alice": {"math": 85, "science": 90},
    "Bob": {"math": 70, "science": 60}
}

# Nested for loops

# Accessing outer dictionary . dict.items() to access both keys and values
for name, inner_dict in students.items():
    print("\nStudent :", name)
    print("Subjects and Scores :")

    # Accessing inner dictionary. dict.items() to access both keys and values
    for subject, score in inner_dict.items():
        print(subject,":", score)