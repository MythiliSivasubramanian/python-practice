# Flattening Lists

# Sample input: nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]] Sample output: [1, 2, 3, 4, 5, 6, 7, 8]

# Predefined nested list
x = [[1, 2, 3], [4, 5], [6, 7, 8]]
print("\nInitial list is  : ",x)

# List comprehension
flatted_llist = [n for sublist in x for n in sublist]
print("\nFlat list : ",flatted_llist )
