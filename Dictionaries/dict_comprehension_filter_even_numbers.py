# Creating a dictionary from a predefined list,
# filtering only even numbers using dictionary comprehension

# Predefined list of numbers
numbers_list = [1, 2, 3, 4, 5, 6]

# Dictionary comprehension:
# - includes only even numbers : keys are the even numbers and values are double of the keys
my_dict = {i: i * 2 for i in numbers_list if i % 2 == 0}

print(my_dict)
