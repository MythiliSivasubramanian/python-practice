"""
Simple Calculator Program:
Addition, Subtraction, Multiplication, Division, Modulus, and Power.

It uses:
- Functions for each operation
- A dictionary to map operators to functions
- User input for numbers and operator
"""

# Returns the sum of two numbers
def add(a, b): 
    return a + b 

# Returns the difference of two numbers   
def sub(a, b): 
    return a - b

# Returns the product of two numbers
def mul(a, b): 
    return a * b

# Returns the result of division. Handles division by zero.
def div(a, b): 
    return "Error: divide by zero" if b == 0 else a / b

# Returns the remainder of a divided by b.
def mod(a, b): 
    return a % b

# Returns a raised to the power of b
def power(a, b): 
    return a ** b

# Main function
if __name__ == "__main__":
    
    # Read user inputs
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operator (+ - * / % ^): ")
    
    
    # Dictionary mapping operators to functions
    ops = {"+": add, "-": sub, "*": mul, "/": div, "%": mod, "^": power}
    
    # Perform operation if valid operator is provided
    if op in ops:
        print("Result:", ops[op](a, b))
    else:
        print("Invalid operator")
