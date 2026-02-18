"""
Multiple Checker: 3 or 7
Checking whether a given number is a multiple of 3 or 7.
"""
# Prompting the user to enter a number
num = int(input("Enter a number: "))

# Checking if divisible by 3 or 7
if num % 3 == 0 or num % 7 == 0:
    print("Multiple of 3 or 7")
else:
    print("Not a multiple of 3 or 7")
