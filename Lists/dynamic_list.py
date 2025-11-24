# Dynamic List + Total Calculator

default_list = []
user_input = int(input("Enter the number to be added to the list : "))
default_list.append(user_input)
print("Updated list is : ",default_list)

user_choice = input("Would you like to add other number to the existing list? (yes/no): ").lower()

while user_choice == "yes":
    user_input = int(input("Enter the number to be added to the list : "))
    default_list.append(user_input)
    print("Updated list is : ", default_list)
    user_choice = input("Would you like to add other number to the existing list? (yes/no): ").lower()

print(f"\nSummary:\nYou entered {len(default_list)} numbers.\nFinal List is : {default_list}\nSum of all items in list is : {sum(default_list)}\nGood Bye")
