"""
Password Strength Checker :
Evaluates the strength of a password based on:
- Minimum length (8 characters)
- Digits
- Uppercase letters
- Lowercase letters
- Special characters
Based on these, the password is classified as: Strong, Medium, or Weak.
"""

import string

def password_strength(password):
    """
    Evaluate the strength of a password.
    Returns strength level of the password. Strong,Medium or weak
    """
            
    length_ok = len(password) >= 8
    digit_ok = any(char.isdigit() for char in password)
    upper_ok = any(char.isupper() for char in password)
    lower_ok = any(char.islower() for char in password)
    special_ok = any(char in string.punctuation for char in password)

    score = sum([length_ok, digit_ok, upper_ok, lower_ok, special_ok])

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Medium"
    else:
        return "Weak"

print("=== Password Strength Checker ===")

while True:
    pwd = input("Enter a password: ")

    if pwd.strip() == "":
        print("Password cannot be empty. Try again.")
        continue

    result = password_strength(pwd)
    print(f"Password Strength: {result}")

    again = input("Check another? (y/n): ").lower()
    if again != "y":
        break
