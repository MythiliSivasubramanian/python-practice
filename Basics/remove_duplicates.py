def remove_duplicates(items):
    """Return a new list with duplicates removed."""
    unique = []
    for i in items:
        if i not in unique:
            unique.append(i)
    return unique

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
