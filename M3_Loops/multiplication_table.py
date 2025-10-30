# to print multiplication table for a given number

# Get a number from the user as input
num = int(input("Enter a number: "))

# Printing the table up to 10
print(f"\nMultiplication Table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
