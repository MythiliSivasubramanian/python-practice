# 07_file_system_operations.py
# Learning file & folder operations using os module


import os   # os = operating system module

#  Get current working directory

current_path = os.getcwd()

print("Current working directory:")
print(current_path)


# List files & folders


items = os.listdir()

print("\nFiles & folders in this directory:")
print(items)



# Check if file exists


file_name = "demo.txt"

if os.path.exists(file_name):
    print(f"\n{file_name} exists ")
else:
    print(f"\n{file_name} does NOT exist ❌")



# Create a new folder


folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("\nFolder created")
else:
    print("\nFolder already exists")



#  Rename a file

# First create a file to rename

with open("old_name.txt", "w") as file:
    file.write("This file will be renamed")

os.rename("old_name.txt", "new_name.txt")

print("\nFile rename")



#  Delete a file


if os.path.exists("new_name.txt"):
    os.remove("new_name.txt")
    print("File deleted ")
else:
    print("File not found")