# number guessing game
secret_number = 7
user_number = int(input("Welcome to number guessing Game.\nGuess the number from 1 to 10, which is in my mind : "))

while secret_number != user_number:

    if user_number > secret_number:
        print("Too high. Try again")

    elif user_number < secret_number:
        print("too low. Try again")
      
    user_number = int(input("New number : "))
  
print("Congratulations, you guessed the number correctly ")
