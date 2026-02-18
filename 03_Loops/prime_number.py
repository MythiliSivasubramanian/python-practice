# To check if the given number is prime number

def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check divisibility up to the square root of the number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # If divisible by any number, it's not prime
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
