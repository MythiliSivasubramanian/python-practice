expenses = []

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount (€): "))
    expenses.append((name, amount))
    print("Expense added.")

def view_expenses():
    print("\n--- Expense List ---")
    total = 0
    for item, cost in expenses:
        print(f"{item} - €{cost:.2f}")
        total += cost
    print("--------------------")
    print(f"Total: €{total:.2f}\n")

def main():
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
