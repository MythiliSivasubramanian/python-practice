# Reverse the string without suing predefined functions like reversed() or [::-1]

user_string = input()

new_string = ""

for char in user_string:
    new_string = char + new_string
print(new_string)
