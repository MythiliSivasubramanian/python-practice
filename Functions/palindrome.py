def is_palindrome(text):
    """Check if text is a palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("Race car"))
