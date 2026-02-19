""" Get name , age and height as input 
Use an f-string to print: My name is name, I am age years old and 0.00 meters tall. The Height is to be shown with 2 decimal places. """

users_name = input("Enter Name : ")
users_age = int(input("Enter age : "))
users_height = float(input("Enter height (meters) in decimal eg 1.68 : "))

print(f"My name is {users_name}, I am {users_age} years old and {users_height :.2f} meters tall.")
