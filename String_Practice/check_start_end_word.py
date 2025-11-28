"""Check if a string starts with "Hello" and ends with "!" Sample Input: "Hello World!" → Output: True
Input: "Hi there!" → Output: False"""

user_text = input("Enter a string with more than 2 words separated by space : ")
start_text = input("Enter the start term : ")
end_text = input("Enter the end term : ")
print(user_text.startswith(start_text) and user_text.endswith(end_text))
