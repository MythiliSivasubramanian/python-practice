"""
From a nested list, ignore numbers divisible by 3, double even numbers,square odd numbers
Output should still be single flat list.
"""

# Predefined nested list
nested = [[1, 2, 3], [4, 5, 6]]
print("\nInitial list is : ",nested)

result = [
    num * 2 if num % 2 == 0 else num ** 2
    for sublist in nested
    for num in sublist
    if num % 3 != 0
]
print("\nResult: Ignore numbers divisible by 3, double even numbers,square odd numbers : ",result)
