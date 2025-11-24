# Find the smallest positive number from a list

def smallest_positive(nums):
    smallest = None

    for n in nums:
        if n > 0:
            if smallest is None or n < smallest:
                smallest = n

    return smallest

print(smallest_positive([3, -1, 0, 5, 2, -4]))
