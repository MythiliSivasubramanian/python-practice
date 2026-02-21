# 04_with_statement.py
# Goal: Using"with open()' for safe file handling



# Write using WITH

# "with" automatically closes the file
# No need to write file.close()

with open("with_demo.txt", "w") as file:
    file.write("Line 1: Using with statement\n")
    file.write("Line 2: File auto closes\n")

print("File written using WITH")



# Read using WITH


with open("with_demo.txt", "r") as file:
    content = file.read()
    print("\nFile content:")
    print(content)



# Append using WITH


with open("with_demo.txt", "a") as file:
    file.write("Line 3: Appended safely\n")

print("New line appended ")



# Read again to confirm


with open("with_demo.txt", "r") as file:
    print("\nUpdated content:")
    print(file.read())