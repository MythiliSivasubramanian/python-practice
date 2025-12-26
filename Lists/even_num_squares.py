# Filter even numbers and generate a list of their squares
# Method 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("\nInitial numbers list is : ",numbers)
# List comprehension

squares_even_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print("\nList of squares of even numbers in the list : ",squares_even_numbers)

# Method 2

even_squares = [num ** 2 for num in range(1,21) if num % 2 == 0]
print("\nList of squares of even numbers in the list : ",even_squares)
