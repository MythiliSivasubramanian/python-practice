#  Remove duplicates from a list
numbers = [1, 2, 3, 2, 4, 1, 5]
unique_numbers = list(dict.fromkeys(numbers))
print("Unique numbers:", unique_numbers)
