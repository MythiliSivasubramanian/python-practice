# Iterating over a dictionary by using .items() to access both keys and values

# Creating a dictionary with 3 keys value pairs
student = {
    "name": "Emma",
    "age": 19,
    "grade": "A"
}

# Iterating the pairs in dictionary using for loop
# .items() to iterate both keys and values
print("\nIterating over both keys and values: ")
for key, value in student.items():
    print(key, ":", value)
    

# Iterating only keys from dictionary
print("\nIterating over only keys: ")
for keys in student:     # Same as for keys in student.keys():
    print(keys)

# Another method to get all keys from a dictionary as a list
print("\nAll keys of dictionary using .keys() : ",list(student.keys()))