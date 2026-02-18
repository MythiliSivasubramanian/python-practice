def remove_duplicates(items):
    """Return a new list with duplicates removed."""
    unique = []
    for i in items:
        # add item only if not already seen
        if i not in unique:
            unique.append(i)
    return unique

# Test the function with some sample input
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
