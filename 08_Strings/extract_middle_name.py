"""Given a full name John Michael Doe, extract only the middle name. Sample Input: "John Michael Doe"
Sample Output: Michael """

# Method 1 using list
user_name = list(input("Enter First, Middle, Last name separated by space : ").split(" "))
print(user_name[1])

# Method 2 using find()
name = input("Enter First, Middle, Last name separated by space : ")
first_space = name.find(" ")
middle_last_name = name[first_space +1:]
second_space = middle_last_name.find(" ")
last_name = middle_last_name[:second_space]
print(last_name)
