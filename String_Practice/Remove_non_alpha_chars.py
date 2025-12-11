""" Remove the non-alpha characters from the given string . Eg Sample input : <<<Python>>>
Sample output : Python """

my_string = "<<<Python>>>"
# Method 1
print(my_string[3:9])

# Method 2 
users_string = input("Enter a String with symbols  : ")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
new_string = ""
for ch in users_string:
	if ch in alpha:
		new_string += ch
print(new_string)
