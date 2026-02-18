"""
From a list of numbers:
if index is even → square the value
if index is odd → double the value
print index + final value

"""


# Predefined list of numbers
numbers = [1, 2, 3, 4, 5]

for index, value in enumerate(numbers):
    if index % 2 == 0:
        print("Index",index, "→", value ** 2)
    else:
        print("Index",index, "→", value * 2)
