 # 02_read_methods.py
 # Goal: different ways to READ a file



 # Create sample file first (So read mode won’t fail)


file = open("sample_read.txt", "w")
file.write("Line 1: Python\n")
file.write("Line 2: File Handling\n")
file.write("Line 3: Reading Methods\n")
file.close()

print("\nSample file created. \n")



# read() → Reads FULL file Returns entire content as ONE string

file = open("sample_read.txt", "r")
content = file.read()
print("Using read():")
print(content)
file.close()


# readline() → Reads ONE line Each call reads next line

file = open("sample_read.txt", "r")
print("\nUsing readline():")

line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)

file.close()



# readlines() → Reads ALL lines. Returns list of lines

file = open("sample_read.txt", "r")
lines = file.readlines()
print("\nUsing readlines():")
print(lines)    # list output
file.close()



# Loop through file . Memory efficient for large files

file = open("sample_read.txt", "r")
print("\nReading using loop:")

for line in file:
    print(line.strip())  # strip() removes newline \n
file.close()