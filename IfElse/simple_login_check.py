"""
Simple Login Validation
"""
# Taking user input
username = input("Enter username: ")
password = input("Enter password: ")

# Validating credentials using equality operator 
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid login")
