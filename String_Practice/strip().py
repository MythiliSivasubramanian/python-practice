my_string = "   Sample Text   "
second_string = "\n\t  Python  \t\n"
# Remove only the starting and ending spaces from my_string
print(my_string.strip())
print(second_string.strip())

# Remove # from the both front and end
text = "## Hello ##"
print(text.strip("#"))

# Remove whitespace from the left only
print(my_string.lstrip())
print(second_string.lstrip())

# Remove whitespace from the right only
print(my_string.rstrip())
print(second_string.rstrip())

#Remove the "abc" if any in front or end :
user_string = "abHello World greata!Ac"
print(user_string.strip("abc"))



