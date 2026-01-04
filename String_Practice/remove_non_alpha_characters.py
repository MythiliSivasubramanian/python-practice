""" Convert "23°C" to "23C" (remove non-alphabetic characters like °). Sample Input: "23°C"  Sample Output: 23C """
import re

user_input = input("Enter a word with non - alphabetic characters eg 23°C : ")

# Method 1: using isalphanum(). Drawback result without space
print("".join(char for char in user_input if char.isalnum()))

# Method 2: replace substitute re.sub() :
print(re.sub(r'[^a-zA-Z0-9]', '', user_input))

