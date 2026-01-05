"""
Simple ATM Program :

Allows the user to:
1. Deposit money
2. Withdraw money
3. Check current balance
4. Exit the program

Concepts used:
- Functions
- While loop
- Conditional statements
- Exception handling
- User input validation
"""

# Initial account balance
balance = 0.0

# Function to display the ATM menu options to the user.
def show_menu():
    print("\n=== Simple ATM ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            balance += amount
            print(f"Deposited {amount:.2f}€. New balance: {balance:.2f}€")
        except ValueError:
            print("Invalid amount.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrawn {amount:.2f}€. New balance: {balance:.2f}€")
        except ValueError:
            print("Invalid amount.")

    elif choice == "3":
        print(f"Current balance: {balance:.2f}€")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid option. Please try again.")
