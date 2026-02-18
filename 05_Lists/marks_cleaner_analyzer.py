"""
Topic  : Python Lists
Level  : Beginner Maintenance Practice
Task   : Marks Cleaner + Analyzer
Skills : List comprehension, filtering, classification, min/max manual logic.
"""

"""
Task: “Marks Cleaner + Analyzer”
You’re given a raw marks list (messy data )
marks = [78, 45, 92, 60, 30, 88, 45, 0, 100, 67]

Task 1 — Remove Invalid Marks. Remove marks that are: Equal to 0
Create a new list with correct marks without 0
"""

# Predefined list of marks 
# Mess with invalid mark 0
marks = [78, 45, 92, 60, 30, 88, 45, 0, 100, 67]

# Create a new list after removing invalid marks '0'
cleaned_marks = [   mark # Required expresion
                    for mark in marks  # Loop. for each mark(element) in list marks
                    if mark != 0 # Condition filtering (filter marks greater than 0)
                 ]

# Print original marks and cleaned marks
print("\n\nOriginial Marks :\n", marks, "\n\nCleaned_marks :\n",cleaned_marks)

"""
Task 2 — Classify Pass / Fail
Rules: Pass ≥ 50 Fail < 50
Create two lists: pass_list = ? fail_list = ?
"""

pass_list = [mark for mark in cleaned_marks if mark >= 50]
fail_list = [mark for mark in cleaned_marks if mark < 50]

print("\nCount of pass marks (Pass ≥ 50) :", len(pass_list))
print("\nCount of fail marks Fail < 50 :", len(fail_list))

"""
Task 3 — Find Highest & Lowest (No shortcuts) Do not use max() or min().
"""

# Let the 1st element in list be the highest and lowest
highest_marks = cleaned_marks[0]
lowest_marks = cleaned_marks[0]

for mark in cleaned_marks:
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark

# Print highest and lowest mark
print("\nHighest mark is :", highest_marks)
print("\nLowest mark is :", lowest_marks)
    
"""
Task 4 — Average Marks. Calculate average of cleaned list. Round to 2 decimals.
"""
# Calculate the Average mark
Average_mark = sum(cleaned_marks)/len(cleaned_marks)
print(f"\nAverage mark : {Average_mark:.2f}\n")
