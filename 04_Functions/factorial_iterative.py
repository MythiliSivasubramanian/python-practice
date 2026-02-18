"""
Factorial Calculator :
A function to compute the factorial of a non-negative number n.
"""

# Function to compute factorial
def factorial(n):
    """Return factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
