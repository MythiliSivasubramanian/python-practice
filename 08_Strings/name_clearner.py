"""
File        : name_cleaner.py
Topic       : Python Strings
Practice    : String Cleaning & Standardization

Problem:
Given a messy list of names containing:
- Leading spaces
- Trailing spaces
- Mixed letter cases

Example Input:
names = ["  anu", "BALA  ", "  Cathy ", "david", "EVA  "]

Objectives:
1. Remove leading and trailing spaces 
2. Standardize all names 
3. Count total characters of each name and across cleaned names
4. Find the longest name without using max()

Concepts Covered:
- String strip()
- Case conversion (title)
- List traversal
- Length calculation
- Manual max-length logic

"""


# Predefined list of names
names = ["  anu", "BALA  ", "  Cathy ", "david", "EVA  "]
print("\n\nPreadefined messy list of names :", names)


# Clean leading and trailing spaces
cleaned_names = []

for name in names:
    cleaned_names.append(name.strip())
print("\nCleaned list of names without extra spaces : ", cleaned_names)


# Standardize Case
standardized_names = []
for name in cleaned_names:
    standardized_names.append(name.title())
print("\nList with Standardize Case :", standardized_names)

# Count total characters of each name
print("\nLength of each names :")
for name in standardized_names:
    print(name, "->", len(name))
    
# Count of all characters of standardized_names
all_chars_count = 0

for name in standardized_names:
    all_chars_count += len(name)
print("\nCount of all characters in the list is :", all_chars_count)
    
# Find the longest name with max()
print("\nLongest name in the list and its count of characters : ")
longest_name = standardized_names[0] # 3
for name in standardized_names:
    if len(name) > len(longest_name):
        longest_name = name
print(longest_name, len(longest_name),"\n")