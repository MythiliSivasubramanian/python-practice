#Even and Odd Number Operations : Double the even numbers, Square the odd numbers 
#List comprehen with two conditions in one go

# Function to double the even numbers
def double_even(x):
    return x * 2

# Function to square the odd numbers
def square_odd(x):
    return x ** 2

# Predefined list 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nThe inital list is : ",numbers)

# List comprehension
Result = [double_even(num) if num % 2 == 0 else square_odd(num) for num in numbers]

print("\nResult with even numbers doubled and odd numbers squared : ",Result)

