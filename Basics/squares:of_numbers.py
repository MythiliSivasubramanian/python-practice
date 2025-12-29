# Find squares of numbers in a list

def square_numbers(nums):
    # list to store squared values
    squares = []
    for n in nums:
        squares.append(n ** 2)
    return squares

# Test the function with some random sample list of numbers
print(square_numbers([1, 2, 3, 4, 5]))
