def find_max(numbers):
    """Return the highest number from a list."""
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print(find_max([3, 8, 2, 10, 6]))
