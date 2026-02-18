"""
Divisibility Checker :
Checking whether a given number is divisible by both 5 and 11.
"""

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Checking divisibility by 5 and 11
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")
