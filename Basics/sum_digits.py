def sum_of_digits(n):
    """Return the sum of digits of n."""
    return sum(int(d) for d in str(n))

print(sum_of_digits(9875))
