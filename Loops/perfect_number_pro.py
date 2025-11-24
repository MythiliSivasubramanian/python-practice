# Perfect number checker
import string

# Function to check if the given number is a perfect number
def is_perfect(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i

# Returns True if its a perfect number
    if total == number:
        return True
    else:
        return False

# Prompt and validate the input
def prompt_validate_input(prompt):
    while True:
        try:
            usr_input = int(input(prompt))
            return usr_input
        except ValueError:
            print("Enter a valid number")

# Function to print the results
def print_perfect_not(num,states):
    if states:
        print(f"{num} is a perfect number! ")
    else:
        print(f"{num} is not a perfect number!")



def main():
    prompt_text = "Enter a number to check if its a perfect number : "
    user_input = prompt_validate_input(prompt_text)
    is_perfect_state = is_perfect(user_input)
    print_perfect_not(user_input,is_perfect_state)

# Choice to check another number
    choice = input("Would you like to check another number? (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)

# Loop for getting input multiple times

    while choice == "yes":
        # prompt and validate the input
        user_input = prompt_validate_input(prompt_text)
        # check if perfect
        is_perfect_state = is_perfect(user_input)
        #print result
        print_perfect_not(user_input,is_perfect_state)
        # Ask if user wants to check another number
        choice = input("Would you like to check another number? (yes/no) : ").strip().lower().strip(string.whitespace + string.punctuation)
    print("Thank you and Good day!")

if __name__ == "__main__":
    main()
