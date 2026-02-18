# Create a set of squares using set comprehension
squares = {x**2 for x in range(1, 11)}
print("Squares:", squares)

# Filter example: even numbers from 1 to 10
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print("Even numbers:", even_numbers)

# Filter example: remove duplicates from a list using set comprehension
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = {x for x in nums}
print("Unique numbers from list:", unique_nums)
