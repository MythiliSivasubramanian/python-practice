""" From a list of numbers, multiply each number by its index and 
store the results in a list using list comprehension + enumerate.
"""

# Predefined list
numbers = [5, 10, 15, 20]
print("\nPredefined list is : ",numbers)

result = [index * value for index, value in enumerate(numbers)]
print("\nList of numbers where values multiplied by thier index : ",result)
