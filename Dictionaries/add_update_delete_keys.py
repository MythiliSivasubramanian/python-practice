# Adding, updating, and deleting elements

profile = {
    "username": "coder123",
    "language": "Python"
}

# Add a new key
profile["experience"] = "Beginner"

# Update a value
profile["language"] = "Python 3"

# Delete a key
del profile["username"]

print(profile)
