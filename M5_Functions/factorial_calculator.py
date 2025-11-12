# Factorial Calculator
import string

# 2.2.1 Function to calculate the Factorial of a given number
def factorial_calc(number):
    total = 1
    for i in range (number,0,-1):
        total *= i
    return total

# 2.1.1 Function to prompt and validate if its positive number
def get_input_validate(prompt):
    while True:
        try:
            user_number = int(input(prompt))
            if user_number >= 0:
                return user_number
            else:
                print("Enter a valid positive number! (Number grater than 0)!")
        except ValueError:
            print("Invalid input. Please enter a valid positive number!")


# 2 Call the main function
def main():
    # 2.1 Call input function
    prompt_text = "Enter a positive number to find out its Factorial : "

    while True:
        user_input = get_input_validate(prompt_text)

        # 2.2 call function to get Factorial of the number
        factorial_results = factorial_calc(user_input)

        # 2.3 Print the results
        print(f"Factorial of {user_input} is : {factorial_results}")

        # 2.4 Choice to get Factorial for other number
        choice = input("Would you like to check Factorial for another number? (yes/no) :").lower().strip().strip(string.punctuation)
        if choice == "no":
            break

    print("Thank you and Good day!")

# 1. Call the main function
if __name__ == "__main__":
    main()
