# Basic Set Union

# Create two sets:  set_1 and set_b with 2 common elements
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#union_set is set_a + set_b (Duplicates are not allowed in sets)
union_set = set_a | set_b

print("\nSet A:", set_a)
print("\nSet B:", set_b)
print("\nunion_set = set_a | set_b")
print("\nUnion:", union_set,"\n")