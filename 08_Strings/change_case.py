

"""Convert a string to uppercase, then lowercase, then title case.
Sample Input: "python is fun"  Sample Output:
Uppercase: PYTHON IS FUN
Lowercase: python is fun
Title Case: Python Is Fun"""

user_input = input("Enter a String : ")
print(f"{user_input.upper()}\n{user_input.lower()}\n{user_input.title()}")
