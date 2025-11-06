# A simple expenses tracker to add, view expenses, total and quit

expenses = []

def add_expense():
    try:
        entry = input("Enter expense and amount separated by comma (e.g. Coffee, 3.5): ")
        name, amount = entry.split(",")
        name = name.strip()
        amount = float(amount.strip())
        expenses.append([name, amount])
        print(f"Added: {name} - €{amount}")
    except ValueError:
        print("Invalid input! Please enter data in the format: name, amount")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nYour Expenses:")
        for i, (name, amount) in enumerate(expenses):
            print(f"{i}. {name} - €{amount}")
        print()  # extra line for neat spacing


def view_total():
    if not expenses:
        print("No expenses to total yet.")
    else:
        total = sum(amount for _, amount in expenses)
        print(f"Total spent: €{total:.2f}")

while True:
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        view_total()
    elif choice == 4:
        print("Thank you for using Expense Tracker! Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 4.")
