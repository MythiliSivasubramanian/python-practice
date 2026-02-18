"""
Armstrong number checker : 
Armstrong number is a number that equals the sum of its own digits, 
each raised to the power of the total number of digits in the number. 
Ex. 153 : 3 digits : (1^3 + 5^3+ 3^3 =1 + 125 + 27 = 153). 
- Checks if the user's input is a Armstrong number.
- Input validation
- Allows to check the numbers for multiple times
"""


import string

# Function to check if its an Armstrong number
def is_armstrong(number):
    temp= 0
    no_digits = len(str(number))
    for i in str(number):
        temp += int(i)**no_digits
        # Return True if number is Armstrong, else False
    if temp == number:
        return True
    else:
        return False

 # Function to print the results
def print_result(num,states):
    if states:
        print(f"\n{num} is an Armstrong number! ")
    else:
        print(f"\n{num} is not an Armstrong number!")

# Prompt and validate the user input
def prompt_validate_input(prompt):
    while True:
        try:
            user_number = int(input(prompt))
            return user_number
        except ValueError:
            print("\nInvalid input! Enter a valid number\n")

# Defining the main function
def main():
    prompt_text = "\nEnter a number to check if its an Armstrong number : "
    # Prompt and validate the input
    user_input = prompt_validate_input(prompt_text)

    # Check if its a Armstrong number . If return value is true, then its a Armstrong number.
    result_state = is_armstrong(user_input)

    # Print the result
    print_result(user_input,result_state)

    # Choice to check another number
    choice = input("Would you like to check another number? (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)

    # Ask if user wants to check another number
    while choice =="yes":
        user_input = prompt_validate_input(prompt_text)
        result_state = is_armstrong(user_input)
        print_result(user_input, result_state)
        choice = input("\nWould you like to check another number? (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)
    print("\nThank you and Good day!")

# Call the main ()
if __name__=="__main__":
    main()

