def is_valid_email(email):
    """Very Simple email validation check."""
    return "@" in email and "." in email and len(email) > 5

# Testing the function with some sample data
print(is_valid_email("user@example.com"))
