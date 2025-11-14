# Multiplication table generator
import string


# 2.3.1 Multiplication table generater
def  multiplication_table(startnum,stopnum):
    total = 0
    table = []
    for i in range(1,stopnum+1):
        total = i * startnum
        table.append(f"{i} * {startnum} = {total}")
    return table

# 2.2.1 Define tables function
def start_end_tables(starttable,endtable,endnumber):
    all_tables = []
    for i in range(starttable,endtable + 1):
        # Call Multiplication table function to generate the table for i
        table = multiplication_table(i,endnumber)
        all_tables.append(f"\nTable of {i}")
        all_tables.append("----------------")
        all_tables.extend(table)

        if i != endtable:
            all_tables.append("\n****************\n")
    return all_tables





# 2.1.1 Define input function
def get_input(prompt1,prompt2,prompt3):
    while True:
        try:
            start_table = int(input(prompt1))
            if start_table > 0:
                tables_end = int(input(prompt2))
                if tables_end >= start_table:
                    end_num = int(input(prompt3))
                    if end_num > 0:
                        return start_table,tables_end,end_num
            else:
                print("Invalid number. Please enter a number greater than 0!")
        except ValueError:
            print("Invalid Input. Please enter a number greater than 0!")





# 2. Define Main function
def main():
    print("Multiplication Table generator. \nEg If start Table number as 2, end table number as 5, end number as 10, it would prints tables of 2,3,4,5 until 10 each table")
    while True:
        prompt_text_1 = "\nEnter the start table number : "
        prompt_text_2 = "\nEnter the end table number : "
        prompt_text_3 = "\nUntil how many numbers you want for each table : "


        # 2.1 Call Input function
        table_start,end_table,end_number = get_input(prompt_text_1,prompt_text_2,prompt_text_3)

        # 2.2 Call Multiplication function
        result = start_end_tables(table_start,end_table,end_number)

        # 2.3 prints tables
        print("\n".join(result))

        # Choice to check for another multiplication table
        choice = input("\nWould you like to check for another number (yes/no) : ").lower().strip().strip(string.punctuation)
        if choice == "no":
            print("Thank you and Good day!")
            break

# 1. Call main function
if __name__ == "__main__":
    main()
