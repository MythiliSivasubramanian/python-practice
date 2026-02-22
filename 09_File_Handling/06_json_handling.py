# 06_json_handling.py
# Goal: Reading and writing JSON files in Python


import json   # JSON module

# Python data → JSON file

# Creating Python dictionary
student_data = {
    "id": 1,
    "name": "Rose",
    "score": 95,
    "subjects": ["Math", "Python", "SQL"]
}

# Writing dictionary to JSON file

with open("student.json", "w") as file:

    json.dump(student_data, file, indent=4)
    # dump() writes Python data → JSON file
    # indent=4 makes file readable (pretty format)

print("JSON file written")


# Read JSON file → Python data

with open("student.json", "r") as file:

    data = json.load(file)
    # load() reads JSON → Python dictionary

print("\nReading JSON content:")
print(data)


#  Access values from JSON data

print("\nStudent Name:", data["name"])
print("Subjects:", data["subjects"])