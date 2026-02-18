"""
Removing key value pair from a dictionary
- Using pop
- Using del
"""

# Creating a dictionary with 3 key value pairs
student = {
    "name": "Sara",
    "age": 21,
    "city": "London"
}
print("\nActual Dictionary is : ",student)

# Method 1:
# Removing key 'city' using pop(). pop() removes the key and returns its value
removed = student.pop("city")
print("Removed value is : ",removed)


# Method 2:
# Removing key 'age' using del. del removes the key but doesn't return its value
del student["age"]

# Printing final dictionary
print("\nFinal dictionary after removing the keys 'city' and 'age' : ",student)
