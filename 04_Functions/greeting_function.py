#simple function with return value
def greeting():
    name = input("Enter your name: ")
    return name

user_name = greeting()
print(f"Hello {user_name}, welcome back!")
