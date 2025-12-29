# Compute factorial of a number using loop

def factorial(n):
    # assumes n is a non-negative integer
    # start with 1 because factorial multiplies numbers
    result = 1 

    for i in range(1, n + 1):
        # multiply result by current number
        result *= i

    return result
    
# Test the function
print(factorial(5))
