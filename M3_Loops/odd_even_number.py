# Finding out the given number odd or even

def get_valid_input():
    while True:
        try:
            user_input = int(input("Enter a valid number : "))
            return user_input

        except ValueError:
            print("Invalid Input. Please enter a valid integer ")

def check_even_odd(number):
    if number % 2 == 0:
        return f"The given number {number} is Even"
    else:
        return f"The given number {number} is Odd"

number = get_valid_input()
result =  check_even_odd(number)
print(result)
choice = input("Would you like to check another number (yes/no) :").lower()

while choice == "yes":
    num1 = get_valid_input()
    res = check_even_odd(num1)
    print(res)
    choice = input("Would you like to check another number (yes/no) :").lower()

print("Thank you")
