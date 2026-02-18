"""
Nested dictionary : Access, validation & Iteration
- Accessing outer dictionary keys using [] and get()
- Accessing inner dictionary keys safely
- Handling missing keys safely
_ Checking key exsistence using membership in operator
- Iterating over keys, values, key value pairs in a nested dictionary.

Expection:
- To print correct values for the exsisting keys
- To handle missing or non exsisting keys safely
- Inner directionary traversal

"""

# Creating a nested dictionary
student = {
    "name": "Rose",
    "marks": {
        "math": 90,
        "cs": 95
    }
}
print("\nNested Dictionary:")
print(student)


# Accessing outer key
print("\n1: Access outer key 'name'")
print("student['name'] :", student["name"])
print("student.get('name') :", student.get("name", "Not Found"))

# Accessing inner key
print("\n2: Access inner key 'math'")
print("student['marks']['math'] :", student["marks"]["math"])
print("student.get('marks').get('math') :", student.get("marks").get("math", "Not Found"))

# Accessing another inner key
print("\n3: Access inner key 'cs'")
print("student['marks']['cs'] :", student["marks"]["cs"])
print("student.get('marks').get('cs') :", student.get("marks").get("cs"))

# Accessing missing or non exsisting inner key safely
print("\n4: Access missing key 'physics'")
print(
    "student.get('marks').get('physics') :",
    student.get("marks").get("physics", "Key not found")
)

# Checking key existence 
print("\n5: Check key existence")
print("'name' in student :", "name" in student)
print("'math' in student['marks'] :", "math" in student["marks"])

# Checking non-existent key
print("\n6: Check non-existent key 'physics'")
print("'physics' in student['marks'] :", "physics" in student["marks"])

# Printing all keys in inner dictionary
print("\n7: Print all keys in marks dictionary")
for key in student["marks"]:
    print(key)

# Printing all values in inner dictionary
print("\n8: Print all values in marks dictionary")
for val in student["marks"].values():
    print(val)

# Printing all key-value pairs
print("\n9: Print key-value pairs in marks dictionary")
for key, val in student["marks"].items():
    print(key, val)

# Checking both outer and inner keys
print("\n 10: Check both outer and inner keys")
print("'marks' in student :", "marks" in student)
print("'cs' in student['marks'] :", "cs" in student["marks"])
