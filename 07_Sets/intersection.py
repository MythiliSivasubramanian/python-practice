# Find common numbers in two lists


# Create List1 and List 2 with 3 common elements
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# Converting lists to sets 
set1 = set(list1)
set2 = set(list2)

# Intersection & of set1 and set2 (common numbers from both sets)
common_numbers = set1 & set2

# Printing the results
print("\nList 1 : ", list1)
print("\nList 2 : ", list2)
print("\nCommon numbers : ", common_numbers)