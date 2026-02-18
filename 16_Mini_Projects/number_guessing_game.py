"""
Number Guessing Game:
Randomly selects a number between 1 and 50.
The user keeps guessing until the correct number is found.
After each guess, clue is given whether the guess is too low or too high.
"""


import random

def play_game():
    # Generate a random number between 1 to 50
    secret = random.randint(1, 50)
    # Tracks the number of attempts made by the user.
    attempts = 0

    print("Guess the number between 1 and 50!")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
