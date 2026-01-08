"""
Password Strength Checker : 

Checks the strength of a given password based on:
- Length (>= 8 characters)
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of digits
- Presence of special characters (punctuation)

It returns one of the levels:
"Very Weak", "Weak", "Medium", "Strong", "Very Strong"
"""


import string

def check_password(p):
 
    # Evaluate the strength of a password and return strength of the password

    score = 0
    
    # check length
    if len(p) >= 8: 
        score += 1
    
    # check for upper case
    if any(ch.isupper() for ch in p): 
        score += 1
    
    # Check for lower case
    if any(ch.islower() for ch in p): 
        score += 1
     
    # Check for digits   
    if any(ch.isdigit() for ch in p): 
        score += 1
    
    # check for punctuation
    if any(ch in string.punctuation for ch in p): 
        score += 1

    # list of possible levels
    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    
    return levels[score]

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Strength:", check_password(pwd))
