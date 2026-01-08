"""
Password and OTP Generator

Allows the user to:
1. Generate a random secure password of a given length
2. Generate a 6-digit numeric OTP

Concepts used:
- random module
- string module
- Functions
"""

import random
import string

# Function to generate a random password using letters, digits, and special characters. 
def generate_password(length=12): # Default length 12
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))
    # returns generated password as string


# Function to generate a 6-digit numeric OTP.
def generate_otp():
    return "".join(str(random.randint(0, 9)) for _ in range(6))
    # returns otp as string

if __name__ == "__main__":
    print("1. Generate Password\n2. Generate OTP")
    choice = input("Choose: ")

    if choice == "1":
        length = int(input("Length: "))
        print(generate_password(length))
    else:
        print(generate_otp())
