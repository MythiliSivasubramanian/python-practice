# 03_write_methods.py
# Different ways to WRITE to a file


# Write using "w" mode. "w" = write mode
# If file exists then content deleted (overwritten)
# If file doesn't exist the new file created

file = open("write_demo.txt", "w")

file.write("Line 1: Python\n")
file.write("Line 2: Writing to file\n")

file.close()

print("File written using 'w' mode")


# Append using "a" mode. "a" = append mode
# Adds content at the end
# Does not delete old content

file = open("write_demo.txt", "a")

file.write("Line 3: Appended line\n")

file.close()

print("File updated using 'a' mode")


# Write + Read using "w+".  "w+" = write AND read
# Overwrites file
# Allows reading after writing

file = open("write_demo_plus.txt", "w+")

file.write("Hello from w+ mode\n")

file.seek(0) # Moves cursor to beginning before reading

"""
When writing: After writing, cursor moves to end. If we try to read immediately then
it may return nothing since cursor was at end.
So we can use file.seek(0) to move cursor to start.
"""

print("\nContent inside write_demo_plus.txt:")
print(file.read())

file.close()