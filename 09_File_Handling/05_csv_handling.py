# 05_csv_handling.py
# basic CSV file handling in Python


import csv   # csv module helps read/write CSV files



# Write data to CSV

# "newline=''" prevents extra blank lines 

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)
    # writer object helps write rows

    # Writing header row : writerow() : Writes one row
    writer.writerow(["ID", "Name", "Score"])

    # Writing multiple rows
    writer.writerow([1, "Rose", 95])
    writer.writerow([2, "John", 88])
    writer.writerow([3, "Emma", 92])

print("CSV file written")



# Read CSV file


with open("students.csv", "r") as file:

    reader = csv.reader(file)
    # reader object reads rows

    print("\nReading CSV content:")

    for row in reader:
        print(row)
        # Each row is a list
