# Check if a string is a palindrome

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()

    return cleaned == cleaned[::-1]

print(is_palindrome("Level"))
print(is_palindrome("Hello"))
