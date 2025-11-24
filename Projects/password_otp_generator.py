import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def generate_otp():
    return "".join(str(random.randint(0, 9)) for _ in range(6))

if __name__ == "__main__":
    print("1. Generate Password\n2. Generate OTP")
    choice = input("Choose: ")

    if choice == "1":
        length = int(input("Length: "))
        print(generate_password(length))
    else:
        print(generate_otp())
