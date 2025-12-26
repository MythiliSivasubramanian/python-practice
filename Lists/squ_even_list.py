# Square of the even numbers from the predefined list of numbers using list comprehension with function and conditions

# Function to return x * 2
def squares(x):
    return x * 2


# Predefined list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print("\nInitial list is : ",numbers)

# List comprehension with function call and if condition to filter even numbers
squares_even_nums = [squares(num) for num in numbers if num % 2 == 0]
print("\n Squares of even numbers from the list : ",squares_even_nums)
