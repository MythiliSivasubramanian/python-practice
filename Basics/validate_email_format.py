def is_valid_email(email):
    """Simple email validation check."""
    return "@" in email and "." in email and len(email) > 5

print(is_valid_email("user@example.com"))
