# Check if a string is a palindrome

def is_palindrome(text):

    # Remove spaces and normalize case
    cleaned = text.replace(" ", "").lower()

    # Compare string with its reverse
    return cleaned == cleaned[::-1]

# Sample random Test cases
print(is_palindrome("Level"))
print(is_palindrome("Hello"))
