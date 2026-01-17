#  Elements present in only one of the sets


# Create 2 sets with 2 common elements
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Symmetric difference (common elements between 2 sets are ignored)
unique_elements = set1.symmetric_difference(set2)

print("Set 1 : ", set1)
print("Set 2 : ", set2)
print("Only in one set : ", unique_elements)
