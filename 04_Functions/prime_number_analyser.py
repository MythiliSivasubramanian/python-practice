# Prime number analyser
import string


# Function to check if its a prime number
def is_prime_calc(number):
    for i in range(2,number):
        if number % i == 0:
            return "not a Prime"
    return "Prime"


# Function to prompt Input and validate if its greater than 1
def get_input_validate(prompt):
    while True:
        try:
            user_number = int(input(prompt))
            if user_number <= 1:
                print("Enter a Integer greater than 1!")
            else:
                return user_number
        except ValueError:
            print("Invalid Input. Please enter a number greater than 1!")

# Define Main function
def main():

    # Prompt input
    prompt_text = "Enter a number greater than 1 to check if its a prime number : "
    while True:
        user_input = get_input_validate(prompt_text)

        # Call function to check if its a Prime number
        is_prime = is_prime_calc(user_input)

        # Print result
        is_prime = is_prime_calc(user_input)
        print(f"The given number {user_input} is {is_prime} number! ")

        # Option to check another number if its a Prime
        choice = input("Would you like to check another number (yes/no) : ").lower().strip().strip(string.punctuation)
        if choice == "no":
            break
    print("Thank you and Good day! ")

# Call main function
if __name__ == "__main__":
    main()
