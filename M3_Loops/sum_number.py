
"""To get the sum of all digits of the given integer input. 
Two ways to calculate the sum of digits of a number.
Type 1: Converting the given number to string and iterate over characters.
Type 2: Using arithmetic operations (modulo and integer division)."""

#Type 1: String Method

def sum_of_digits_str(num):
    
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

# Type 2: Arithmetic Method

def sum_of_digits_math(num):
   
    total = 0
    while num > 0:
        total += num % 10  # Extract last digit
        num //= 10         # Remove last digit
    return total

# Main function

if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("\nResults using two different approaches:")
    print("String Method:   ", sum_of_digits_str(number))
    print("Arithmetic Method:", sum_of_digits_math(number))
