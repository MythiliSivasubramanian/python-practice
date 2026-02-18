"""
From a nested list of numbers:
keep numbers divisible by 3 unchanged
double even numbers
square odd numbers
output must be one flat list
"""

# Predefined List
nested = [[1, 2, 3], [4, 5, 6]]


result = [
    num if num % 3 == 0
    else num * 2 if num % 2 == 0
    else num ** 2
    for sublist in nested
    for num in sublist
]

print(result)
