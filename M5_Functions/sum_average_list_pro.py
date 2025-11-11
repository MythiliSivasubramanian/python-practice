# Sum and average of all numbers in a list
import string

# 4. Function to add items to the list
def add_list(number):
    items = list(map(int, input("Enter the numbers separated by comma : ").split(",")))
    print("Items added successfully!")
    return items

# 6. Function to add all items in list manually
def sum_list(new_lst):
    total = 0
    for i in new_lst:
        total += i
    return total

# Function to find average in a list
def avg_list(nw_list):
    total = 0
    length = len(nw_list)
    for i in nw_list:
        total += i
    return total / length

# 3. Prompt and validate input
def prompt_validate_input(prompt):
    while True:
        try:
            user_number = int(input(prompt))
            return user_number
        except ValueError:
            print("Enter a valid number")

# 5. Option to choose relevant function
def choice_selection(user_choice, lst):
    if user_choice == 1:
        total_sum_list = sum_list(lst)
        print(f"Sum of all items in the list is : {total_sum_list}")
    elif user_choice == 2:
        total_avg_list = avg_list(lst)
        print(f"Average of all items in the list is : {total_avg_list}")
    elif user_choice == 3:
        print("Thank you and Good day!")

# 2. Defining main()
def main():
    prompt_text = "How many items in the list ? : "

    while True:
        no_items = prompt_validate_input(prompt_text)
        new_list = add_list(no_items)

        while True:
            try:
                choice = int(input("\nEnter the relevant number: \n1 for Addition\n2 for Average\n3 for Quit : "))
            except ValueError:
                print("Enter a valid option")
                continue

            if choice == 3:
                print("Thank you and Good day!")
                return  # exit program

            choice_selection(choice, new_list)

            again = input("\nDo you want to perform another operation on the same list? (yes/no): ").lower().strip(string.whitespace + string.punctuation)
            if again != "yes":
                break

        new_list_choice = input("\nWould you like to add a new list (yes/no) : ").lower().strip(string.whitespace + string.punctuation)
        if new_list_choice != "yes":
            print("Thank you and Goodbye!")
            break

# 1. Call main function
if __name__ == "__main__":
    main()
