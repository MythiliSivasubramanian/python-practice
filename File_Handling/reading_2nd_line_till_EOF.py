
""" 
A raw student data .csv file has 1000 rows. 
Path : /Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv
Goal: Ignore header line(1st line) and read until EOF 
"""

# GOAL: IGNORE 1ST LINE AND REWAD UNTIL EOF

# Method 1: 
# Plain file reading using: with open() as f 
# with open() automatically closes the file after use. f is the file object(an iterator over lines)

print("\n\nMethod 1 : with open() as f: next(f)\n\n")
with open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv") as f: 
    next(f) # Moves the file operator forward by 1 line (Skips the 1st line / header line)
    for line in f: # Iterates from 2nd line till EOF
       print(line.strip()) # Removes newline (\n) and extra spaces.

# Opened file is automatically closed
print("\n\n Opened file is automatically closed\n\n")


# Method 2:
# Using readlines() + slicing:
print("\n\nMethod 2 : Using readlines() + slicing:\n\n")
# Opening the file using with open() as f:
with open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv") as f: 
    lines = f.readlines() # Reads entire file including 1st line into a list: [headerline\n,.... EOF]
# Apply slicing on lines
    for line in lines[1:]: # Iterates from Start_index : 1 till EOF
        print(line.strip()) # Removes newline (\n) and extra spaces.

# Opened file is automatically closed
print("\n\n Opened file is automatically closed\n\n")

# Method 3:
# Using enumerate()

print("\n\nMethod 3 : Using enumerate()\n\n")
# Reopeneing the file using with open() as f:
with open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv") as f: 
    for i, line in enumerate(f): # for each index, line in file f
        if i == 0: # index 0 , which is line 1 (headerline)
            continue # Skips the rest of the loop and moves to next iteration
        print(line.strip())

# Opened file is automatically closed
print("\n\n Opened file is automatically closed\n\n")


# Method 4:
# using itertools.islice - iterator-level (file as a stream)
print("\n\nMethod 4 : using itertools.islice  \n\n")
from itertools import islice
# itertool : module for iterator tools
# islice : iterator slice (iterable, start, end)
# Normal slicing first loads file in momory and then slices. But here, its Like slicing but without loading into memory

# Reopening the file 
with open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv") as f: 
    for line in islice(f,1,None): # For each line in islice(iterator,startend, Endindex : None)
        print(line.strip())
    
print("\n\n Opened file is automatically closed\n\n")

# Memory efficient since entire file is not loaded in to memory


# Method 5
# Using csv module
print("\n\nMethod 5 : Using csv module \n\n")
import csv
#  csv : Built-in module for CSV parsing.

# Reopening the File
with open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv",newline = "") as f: 
    reader = csv.reader(f) # reader is the iterator of rows. csv.reader(f) - Converts each line into a list of columns.["John", "Math", "80", "2022"]
    next(reader) # Moves the reader forward by 1 line (Skips the 1st line / header line)
    
    for row in reader:  # for each row in reader
        print(row)
        
print("\n\n Opened file is automatically closed\n\n")

# Method 6
# using pandas (Pandas needs to be installed.)
#Requirements: python 3 or above, vs code -> Terminal -> pip3 install pandas
print("\n\nMethod 6 :using pandas  \n\n")
import pandas as pd
# df is DataFrame (table object)
df = pd.read_csv("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/File_Handling/raw_data.csv")
# pd.read_csv (autimatically reads file, 1st as header and starts reading data from 2nd line)
print(df)
print("--------------------")

