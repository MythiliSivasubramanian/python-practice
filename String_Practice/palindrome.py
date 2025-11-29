""" Check if a string is a palindrome. Sample Input: 1. Racecar  2. Hello . Sample Output: 1. True 2. False"""

user_text = input("Enter a word to check if its a palindrome : ").lower()
# Using reverse Method - Slicing
reversed_text = user_text[::-1].lower()
print(user_text == reversed_text)

