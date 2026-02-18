"""
Fibonacci Sequence Generator :
A function that returns a list of the first n Fibonacci numbers.
"""

# Function to generate Fibonacci number
def fibonacci(n):
    """Return a list containing n Fibonacci numbers."""
    if n <= 0:
        return [] # No numbers for non-positive input
    if n == 1:
        return [0] # Only the first Fibonacci number

    fib = [0, 1]  # Initialize first two Fibonacci numbers
    for _ in range(2, n):
        # Next number is the sum of the last two numbers
        fib.append(fib[-1] + fib[-2])
    return fib

# Testing with predefined sample input '10'
print(fibonacci(10))
