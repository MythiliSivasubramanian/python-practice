""" Creating and Accessing Dictionary. 
Scenario: building a student portal.
Create a dictionary for a student with keys: "name", "age", "courses" (list of enrolled courses).
Access name using all possible ways
Try accessing a non-existent key "grade" ."""

# Creating a Dictionary for student portal
student = {"Name": "Anna", "Age" : 22, "Courses" : "English,German,Chinese"}

# Accessing and printing the values of the specified key "Name"
print(f"\nThe value of the key 'Name' is : {student['Name']}")

print(f"\nThe value of the key 'Name' is : {student.get('Name')}")

