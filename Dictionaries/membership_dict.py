# Checking if key 'age' is a key in a predefined key.
# To check if a key in a dictionary, in (membership)operator can be used


# Creating a dictionary with 3 Key value pairs
student = {
    "name": "Alex",
    "age": 23,
    "course": "Python"
}

# Checking if key 'age' is in student dictionary using membership operator in
if "age" in student:
    print("Age is available")
else:
    print("Age not found")
