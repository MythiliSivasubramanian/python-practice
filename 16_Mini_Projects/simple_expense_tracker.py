"""
Simple Expense Tracker :

Allows the user to:
1. Add expenses with name and amount
2. View all expenses with totals
3. Exit the tracker

Data is stored in memory as a list of tuples (name, amount).
"""
# List to store all expenses as tuples (name, amount)
expenses = []

# Prompt the user to enter an expense and its amount. Adds the expense to the expenses list.
def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount (€): "))
    expenses.append((name, amount))
    print("Expense added.")

# Display all expenses and the total amount spent
def view_expenses():
    print("\n--- Expense List ---")
    total = 0
    for item, cost in expenses:
        print(f"{item} - €{cost:.2f}")
        total += cost
    print("--------------------")
    print(f"Total: €{total:.2f}\n")

def main():
    #  Main menu loop for the expense tracker.
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
