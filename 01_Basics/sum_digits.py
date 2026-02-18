def sum_of_digits(n):
    
    """Return the sum of digits of n (assuming n as a non-negative integer)."""
    return sum(int(d) for d in str(n))

# Test the function with some random sample number
print(sum_of_digits(9875))
