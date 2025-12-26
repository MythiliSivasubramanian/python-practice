# Function to return num * 2
def double(x):
    return x * 2

# Predefined list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension with function call
doubled = [double(num) for num in numbers]
print(doubled)


