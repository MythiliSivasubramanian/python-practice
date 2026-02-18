# Fibonacci Sequence Generator
import string


# 2.4 Function to generate the Fibonacci series
def generate_fibonacci(number):

    fib = [0,1]
    for i in range(2,number):
        next_num = fib[i - 1] + fib[i - 2]
        fib.append(next_num)
    return fib

# 2.2 Function to prompt and validate the user Input
def prompt_validate_input(prompt):
    while True:
        try:
            user_number = int(input(prompt))
            if user_number > 0:
                return user_number
            else:
                print("Enter a valid positive integer")
        except ValueError:
            print(" Invalid Input. Enter a valid number ")


# 2- Define the main function
def main():
    # 2.1 Prompt and get the user input
    prompt_text = f"Fibonacci Sequence Generator\nHow many terms would you like to generate? : "

    while True:
        user_input = prompt_validate_input(prompt_text)
        # 2.3 Call function to generate the Fibonacci sequence
        fibonacci_numbers = generate_fibonacci(user_input)
        print(f"Fibonacci series upto {user_input} is : {','.join(map(str, fibonacci_numbers))}")
        # Choice to generate other series
        choice = input("Do you want to generate another sequence? (yes/no) : ").lower().strip().strip(string.punctuation)
        if choice == "no":
            break
    print("Thank you and Good day!")

# 1. call the main function
if __name__== "__main__":
    main()
