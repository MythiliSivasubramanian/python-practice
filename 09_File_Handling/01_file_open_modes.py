# 01_file_open_modes.py
# Goal:  all ways to open a file in Python

# file = open("demo.txt", "w")

file = open("demo.txt", "w")
print("File created in WRITE mode")
file.close()


"""
Read Mode: "r". Opens file for reading
File MUST exist, otherwise error
"""

file = open("demo.txt", "r")
print("File opened in READ mode")
file.close()   # Always close manually when not using 'with open'

"""
Write Mode: "w". Opens file for writing
If file exists the old content is deleted
If file doesn't exist a new file is created
"""

file = open("demo.txt", "w")
print("File opened in WRITE mode")
file.close() # Always close manually when not using 'with open'


"""
Append Mode : "a" Opens file to add content at the end
Existing content stays safe
"""

file = open("demo.txt", "a")
print("File opened in APPEND mode")
file.close() # Always close manually when not using 'with open'



"""
Exclusive Creation: "x". Creates new file ONLY
If file already exists then error
"""

file = open("demo_new.txt", "x")
print("File created using EXCLUSIVE mode")
file.close()  # Always close manually when not using 'with open'



"""
Read + Write → "r+ "w" Read AND write
File must exist
"""

file = open("demo.txt", "r+")
print("File opened in READ + WRITE mode")
file.close() # Always close manually when not using 'with open'


"""
Write + Read → "w+" "r" Write + read . Overwrites file
"""

file = open("demo.txt", "w+")
print("File opened in WRITE + READ mode")
file.close()

"""
Append + Read → "a+" Append + read
Does not overwrite
"""

file = open("demo.txt", "a+")
print("File opened in APPEND + READ mode")
file.close()