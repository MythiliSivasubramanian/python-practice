# To check if the given input is a perfect number

# Function to check if given number is a perfect number
def perfect_number_calc(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    if total== number:
                return "Perfect"
    else:
        return "Not Perfect"

# Validate the input
def get_user_input():
    while True:
        try:
            user_input = int(input("Enter the number to check if its a Prime number : "))
            return user_input
        except ValueError:
            print("Enter a valid number ")


# Print result
def print_result(num,num_typ):
    if num_typ == "Perfect":
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")


# 1. Get input from user
usr_input= get_user_input()

# 2. Call function to check if its a perfect number
number_type = perfect_number_calc(usr_input)
print_result(usr_input,number_type)

# Loop to check if another number

choice = input("Would you like to check other number? (yes/no) : ").lower()
while choice == "yes":
    usr_input = get_user_input()
    number_type = perfect_number_calc(usr_input)
    print_result(usr_input, number_type)
    choice = input("Would you like to check other number? (yes/no) : ").lower()
print("Thank you")


