"""
Given a list of numbers:
print the index
print the value
print value squared

"""


# Predefined List of numbers
numbers = [2, 4, 6, 8]

for index,value in enumerate(numbers):
    print("Index",index, "→ value",value, "→ square", value ** 2)
