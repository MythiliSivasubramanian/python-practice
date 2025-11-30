"""Check if the string "python" appears in another string (case-insensitive)
Sample Input: 1.  I love Python programming.         2. I love Java
Output: 1.  True                                   2. False"""

user_string = input("Enter a string : ").lower()
word_check = input("Enter the word to check if its in the given string : ").lower()
print("True") if word_check in user_string else print("False")
print(word_check in user_string)
