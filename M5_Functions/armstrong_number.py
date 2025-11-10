# Armstrong number
import string

# Function to check if its an Armstrong number
def is_armstrong(number):
    total,temp= 0,0
    no_digits = len(str(number))
    for i in str(number):
        temp += int(i)**no_digits
    if temp == number:
        return True
    else:
        return False

 # Function to print the results
def print_result(num,states):
    if states:
        print(f"{num} is an Armstrong number! ")
    else:
        print(f"{num} is not an Armstrong number!")

# Prompt and validate the user input
def prompt_validate_input(prompt):
    while True:
        try:
            user_number = int(input(prompt))
            return user_number
        except ValueError:
            print("Invalid input! Enter a valid number")

# Defining the main function
def main():
    prompt_text = "Enter a number to check if its an Armstrong number : "
    # Prompt and validate the input
    user_input = prompt_validate_input(prompt_text)

    # Check if its a Armstrong number . If return value is true, then its a Armstrong number.
    result_state = is_armstrong(user_input)

    # Print the result
    print_result(user_input,result_state)

    # Choice to check another number
    choice = input("Would you like to check another number? (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)

    # Loop for multiple inputs
    while choice =="yes":
        user_input = prompt_validate_input(prompt_text)
        result_state = is_armstrong(user_input)
        print_result(user_input, result_state)
        choice = input("Would you like to check another number? (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)
    print("Thank you and Good day!")

# Call the main ()
if __name__=="__main__":
    main()

