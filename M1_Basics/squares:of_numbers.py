# Find squares of numbers in a list

def square_numbers(nums):
    squares = []
    for n in nums:
        squares.append(n ** 2)
    return squares

print(square_numbers([1, 2, 3, 4, 5]))
