# sum of all items in a list
def calculation(x):
    total = 0
    for i in x:
        total += i
    return total


# get and validate the user input
while True:
    try:
        user_input = list(map(float, input(
            "Enter the valid numbers to be added in the list separated by comma (e.g. 12.8,5,0,-2): "
        ).split(",")))
        print("Your list:", user_input)
        break
    except ValueError:
        print("Enter valid numbers separated by commas (e.g. 12.8,5,0,-2): ")

# call the function
total_list = calculation(user_input)
print("Total of all items in list is:", total_list)
