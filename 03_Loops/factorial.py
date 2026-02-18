# to calculate the factorial of a given number

def factorial(n):
    result = 1
    # Multiply result by each number from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is:", factorial(num))
