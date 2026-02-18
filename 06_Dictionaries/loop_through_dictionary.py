#  Iterating through dictionary using for loop

# Creating a dictionary with 3 key value pairs
marks = {
    "Math": 85,
    "Science": 90,
    "English": 88
}

# Iterating through dictionary using for loop
# dict.items() to access both keys and values
for subject, score in marks.items():
    print(subject, ":", score)
