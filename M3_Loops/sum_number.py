# To find the sum of digits of a given number without sum()

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(number))
