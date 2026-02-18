import random

secret_number = random.randint(1,20)
attempts = 0
print("Welcome to number guessing game")
while True:
    try:
        user_input = int(input("Enter the secret number (1-20) : "))
        attempts += 1
        if user_input < 0 or user_input > 20:
            print("Enter the number within the range (1- 20)")
        elif user_input < secret_number:
            print("Too low. Try again")
        elif user_input > secret_number:
            print("Too high. Try again")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Enter a valid integer : ")
