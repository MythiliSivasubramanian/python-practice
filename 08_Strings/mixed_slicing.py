"""Given a string, print first 3 chars, last 3 chars, and middle chars reversed. Sample Input: DataScience
Output: DateicSance """


user_input = input("Enter a String : ")

first_3_chars = user_input[0:3]
last_3_chars = user_input[-3:]
middle = user_input[3:(len(user_input) - 3)]
middle_rev = middle[::-1]


print((first_3_chars)+(middle_rev)+(last_3_chars))
