# Simple calculator using user input and basic math operations

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get the operation from user to perform
operation = input("Choose operation (+, -, *, /): ")

# Perform the calculation based on user input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Display the result
print("Result:", result)
