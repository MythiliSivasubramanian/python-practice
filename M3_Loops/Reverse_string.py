# reverse the given string

user_string = input("Enter the word or a string")
reversed_string = ""
for i in range(len(user_string)-1,-1,-1):
   reversed_string += user_string[i]

print("Reversed string is ",reversed_string)
