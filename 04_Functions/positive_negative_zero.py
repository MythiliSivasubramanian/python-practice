# find if the input is positive , negative or zero using a function

def find_num_type(a):
    if a > 0:
        num_type = "Positive"
    elif a < 0:
        num_type = "Negative"
    elif a == 0:
        num_type = "Zero"

    return num_type
while True:
    try:
        user_input = int(input("Enter a number : "))
        break
    except ValueError:
        print("Enter a valid number: ")

#call the function

user_number_type = find_num_type(user_input)
print(f"The number {user_input} is {user_number_type}")
