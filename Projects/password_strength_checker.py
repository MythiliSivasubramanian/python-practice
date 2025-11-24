import string

def check_password(p):
    score = 0
    if len(p) >= 8: score += 1
    if any(ch.isupper() for ch in p): score += 1
    if any(ch.islower() for ch in p): score += 1
    if any(ch.isdigit() for ch in p): score += 1
    if any(ch in string.punctuation for ch in p): score += 1

    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    return levels[score]

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Strength:", check_password(pwd))
