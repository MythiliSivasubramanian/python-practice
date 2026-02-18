# Flatten and filter the list only with even numbers

# Predefined list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
print("\nInital list : ",nested_list)

# List comprehension

flat_list = [num for sublist in nested_list for num in sublist if num % 2 == 0]
print("\n Flat list with even numbers only : ",flat_list)
