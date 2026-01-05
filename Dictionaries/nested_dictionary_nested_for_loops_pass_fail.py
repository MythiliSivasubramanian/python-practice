""" Nested Dictionaries – Pass / Fail Conversion
Converting student subject scores either as "Pass" or "Fail". Pass if score >= 60
"""

# Predefined nested dictionary
students = {"Alice": {"math": 85, "science": 90}, "Bob": {"math": 70, "science": 60}}

# New dictionary to store results with score as pass or fail
result = {}

# Using nested for loops
# Outer loop: student name and respective subject dictionary
for name, inner_dict in students.items():
    # creating inner dictionary for each student
    result[name] = {}  

    # Inner loop: subject and score
    for subject, score in inner_dict.items():
        if score >= 60:
            result[name][subject] = "Pass"
        else:
            result[name][subject] = "Fail"

# Final output
print("Result:",result)
