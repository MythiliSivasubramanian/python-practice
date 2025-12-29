# Find the smallest positive number from a list

def smallest_positive(nums):
    # stores the smallest positive number found so far
    smallest = None

    for n in nums:
        # consider only positive numbers only
        if n > 0:
            if smallest is None or n < smallest:
                smallest = n

    return smallest

# Test the function with some sample input
print(smallest_positive([3, -1, 0, 5, 2, -4]))
