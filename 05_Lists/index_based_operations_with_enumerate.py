"""
From a list of numbers, using enumerate() and list comprehension,
If the index is even, square the value.
If the index is odd, double the value.
"""

# Get input as a list .split() converts to list but the values are still string not int
users_input  = input("Enter the numbers separated by comma : ").split(",")

# explicitly convert values of users_input list from strings to int
users_input = [int(x) for x in users_input]

# List comprehension and enumerate
result = [
    value * value if index % 2 == 0
    else value * 2 
    for index,value in enumerate(users_input)
          ]

print("\nIf Even Index : values are squared. If odd Index, values are doubled : Result list is :",result)
