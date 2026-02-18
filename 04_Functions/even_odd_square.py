# finding if the input is even or odd and Square of it

# functioon to find if input is even/odd and square of it
def calculation(a):
    square = a * a
    if a % 2 == 0:
        num_typ = "Even"
    else:
        num_typ = "Odd"
    return num_typ,square


# Get inputs and validate if integers
while True:
    try:
        num_1 = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a valid numbers")

# call the function calculation
number_type,num_square = calculation(num_1)
print(f"The number {num_1} is {number_type} and its square is {num_square}")
