def second_largest(nums):
    """Return the second largest number from a list."""
    unique = list(set(nums))  
    unique.sort(reverse=True)
    return unique[1] if len(unique) >= 2 else None

print(second_largest([4, 1, 9, 3, 9, 7]))
