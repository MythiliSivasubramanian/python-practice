# Generate a list of squares of numbers from 1 to 10
# Method 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num ** 2 for num in numbers]
print("\nList of squares of numbers from 1 to 10 : ",squares)


# Method 2
squ = [num ** 2 for num in range(1,11)]
print("\nList of squares of numbers from 1 to 10 : ",squ)
