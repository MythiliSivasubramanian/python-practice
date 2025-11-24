# To heck if the given number is a even or a odd number
# 3.1 Function to print the results
import string

# Prints if the number is even or odd
def print_even_odd(u_input,types):
    if types:
        print(f"{u_input} is a even number!")
    else:
        print(f"{u_input} is a odd number!")

# 2.2 Function to check if the number is even or odd
def check_even_odd(number):
#Returns True if number is even, False if odd
    return number % 2 == 0


# 1.1 Function to get and validate the user's input
def get_valid_integer(prompt):
    while True:
        try:
            usr_input = int(input(prompt))
            return usr_input
        except ValueError:
            print("Invalid number. Please enter a valid integer ")


# 1. Prompt and get the input
def main():
    prompt_text ="Enter a number to check if its a Even or odd number : "
    user_input = get_valid_integer(prompt_text)
    even_odd_state = check_even_odd(user_input)
    print_even_odd(user_input,even_odd_state)

    choice = input("Would you like to check another number (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)

    while choice == "yes":
        user_input = get_valid_integer(prompt_text)
        even_odd_state = check_even_odd(user_input)
        print_even_odd(user_input, even_odd_state)
        choice = input("Would you like to check another number (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)

    print("Thank you and good day")

# Call main function
if __name__ == "__main__":
    main()


