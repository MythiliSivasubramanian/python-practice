# Multiplication table generater.
import string


# Function to perform the Multiplication
def multiplication_calc(start,end):
    total = 0
    table = []
    for i in range(1,end+1):
        total = i * start
        table.append(f"{i} * {start} = {total}")
    return table

# Function to get and validate the Input function
def get_input(prompt_1,prompt_2):
    while True:
        try:
            user_start_number = int(input(prompt_1))
            if user_start_number > 0:
                user_end_number = int(input(prompt_2))
                if user_end_number > 0:
                    return user_start_number,user_end_number
                else:
                    print("Invalid End number!. Please enter a number greater than 0")
            else:
                print("Invalid Input! Enter a valid number greater than 0!")

        except ValueError:
             print("Invalid Input! Please enter a valid number greater than 0! ")

# main function definition
def main():
    while True:

        # Prompt and validate the user input, start and end number for a multiplication table.
        prompt_text_1 = "Enter a number to see its multiplication table : "
        prompt_text_2 = "Until how many numbers the multiplication table to be generated : "
        start_num,end_num = get_input(prompt_text_1,prompt_text_2)

        # Call the function to perform the multiplication table
        result_table = multiplication_calc(start_num,end_num)

        # Print the results
        print("\n".join(result_table))

        # Choice to check for another multiplication table
        choice = input("Would you like to check for another number (yes/no) : ").lower().strip().strip(string.punctuation)
        if choice == "no":
           print("Thank you and Good day!")
           break

# call the main function
if __name__ =="__main__":
    main()
