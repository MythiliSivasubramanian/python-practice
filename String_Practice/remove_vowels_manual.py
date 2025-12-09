# Remove all vowels from a string without using replace() or regex


vowels = "AEIOUaeiou"
user_string = input("Enter a String : ")
new_string = ""

for char in user_string:
    if char not in vowels:
        new_string += char
print(new_string)
                    
