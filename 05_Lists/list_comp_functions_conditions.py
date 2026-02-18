
# Function to square only the odd numbers from  the predefined nested list
 
def squares(x):
    return x * x

# Predefined nested list
nested_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nInital list is : ",nested_numbers)

# List comprehension to flatten the list
flat_list = [num for sublist in nested_numbers for num in sublist]

# List comprehension on flat_list
odd_squares = [squares(num) for num in flat_list if num % 2 != 0]
print("\nSquares of odd numbers in the list : ",odd_squares)

