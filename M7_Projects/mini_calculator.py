def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "Error: divide by zero" if b == 0 else a / b
def mod(a, b): return a % b
def power(a, b): return a ** b

if __name__ == "__main__":
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operator (+ - * / % ^): ")

    ops = {"+": add, "-": sub, "*": mul, "/": div, "%": mod, "^": power}

    if op in ops:
        print("Result:", ops[op](a, b))
    else:
        print("Invalid operator")
