# Apply a function with multiple conditions on list comprehension
""" 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Write a function that doubles a number if it is even and triples the number if it is odd.
Then, apply this function to the list using a list comprehension, making sure to:
Double the even numbers.
Triple the odd numbers.

"""

def doubles(x):
    return x * 2

def triples(x):
    return x * 3

# predefined list of numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension with function
result_even = [doubles(num) for num in numbers if num % 2 == 0]
result_odd =  [triples(num) for num in numbers if num % 2 != 0]

print("\nDoubles of even numbers : ",result_even)
print("\nTriples of odd numbers : ",result_odd)
