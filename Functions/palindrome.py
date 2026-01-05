"""
Palindrome Checker : Reading backwards and forwards forms the same word
A function to check if a given string is a palindrome.
Ignoring spaces and is case-insensitive.
"""

# Function to check palindrome
def is_palindrome(text):
    """Check if text is a palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# Testing the logic with sample string 'Race car'
print("\nIs the String 'Race car' a palindrome : ")
print(is_palindrome("Race car"))
