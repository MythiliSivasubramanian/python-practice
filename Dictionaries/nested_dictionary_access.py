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

# Task 1: Access outer key
print("\nTask 1: Access outer key 'name'")
print("student['name'] :", student["name"])
print("student.get('name') :", student.get("name", "Not Found"))

# Task 2: Access inner key
print("\nTask 2: Access inner key 'math'")
print("student['marks']['math'] :", student["marks"]["math"])
print("student.get('marks').get('math') :", student.get("marks").get("math", "Not Found"))

# Task 3: Access another inner key
print("\nTask 3: Access inner key 'cs'")
print("student['marks']['cs'] :", student["marks"]["cs"])
print("student.get('marks').get('cs') :", student.get("marks").get("cs"))

# Task 4: Access missing inner key safely
print("\nTask 4: Access missing key 'physics'")
print(
    "student.get('marks').get('physics') :",
    student.get("marks").get("physics", "Key not found")
)

# Task 5: Check key existence
print("\nTask 5: Check key existence")
print("'name' in student :", "name" in student)
print("'math' in student['marks'] :", "math" in student["marks"])

# Task 6: Check non-existent key
print("\nTask 6: Check non-existent key 'physics'")
print("'physics' in student['marks'] :", "physics" in student["marks"])

# Task 7: Print all keys in inner dictionary
print("\nTask 7: Print all keys in marks dictionary")
for key in student["marks"]:
    print(key)

# Task 8: Print all values in inner dictionary
print("\nTask 8: Print all values in marks dictionary")
for val in student["marks"].values():
    print(val)

# Task 9: Print all key-value pairs
print("\nTask 9: Print key-value pairs in marks dictionary")
for key, val in student["marks"].items():
    print(key, val)

# Task 10: Check both outer and inner keys
print("\nTask 10: Check both outer and inner keys")
print("'marks' in student :", "marks" in student)
print("'cs' in student['marks'] :", "cs" in student["marks"])
