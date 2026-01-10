Project:    Smart Data Cleaner & Analyzer (Core Python)
Date: 8 January 2026


Problem Statement:

In the real world, we often work with messy, incomplete (missing values) or unformatted data with inconsistent cases, extra spaces, duplicate records. 

This project focuses on cleaning a raw Student dataset using core Python, so that the cleaned data can be used for further analysis and visualization.


What this Project does:

1.	Reads the student raw data from a text file. The Raw file consist of 1000 records with the 
    following fields Name, Subject, Marks, Year.
    (Raw data file name: raw_data.txt) 
    
2.	Cleans and normalizes the data with consistent casing and removing unnecessary spaces. 

3.	Removes duplicate records after proper normalization.

4.	Handles missing or incomplete data safely using appropriate default values.

5.	Sorts student records in ascending order and assigns sequential roll numbers

6.	Produces a clean, formatted output text file with the following fields:
    First_Name, Last_Name, Roll_No, Subject, Marks, Result, Year.


Assumptions:

1.	Field - Name:
    a)	In the raw file, student name consists of first and last name separated by space.
    b)	Missing First_Name or Last_Name is treated as ‘unknown’

2. Field - Marks:
    a)	Numeric values between 0 and 100.
    b)	Treated as float and rounded to 2 decimal places.
    c)	Missing marks are treated as 0.

3. Field - Result:
   Derived from Marks during data cleaning.
    a)	If Marks > 60 → Pass
    b)	If Marks <= 60 → Fail

4. Field - Year:
    a)	Represents year of examination in YYYY format.
    b)	Missing year is treated as "unknown".

5. Field - Subject:
    a.	Missing subject is treated as "unknown".


Problems Handled:

1.	Duplicate student records removed.
2.	Inconsistent casing in names, subjects are fixed.
3.	Inconsistent spaces from all fields removed
4.	Handled missing data safely (Last_Name, Subject, Marks, Year)
5.	Fixed incorrect data types for all fields:
        a.	Year, Roll_No to int
        b.	First_Name, Last_Name, Subject, Result to string, 
        c.	Marks to float and rounded to 2 decimal points.
6.	Roll numbers are assigned only after cleaning and deduplication.
    Result is derived from Marks during data cleaning.	


Solution Approach:

1.	Reading the data from the student raw text file.
2.	Splitting each record into fields (First_Name, Last_name, Subject, Marks, Year)
3.	Normalizing text fields (case and spacing)
4.	Handling missing values using defaults
5.	Converting cleaned records into immutable structures
6.	Removing duplicates using sets
7.	Sorting records in ascending order on First name and Exam Year
8.	Assigning roll numbers sequentially based on First name


Python Concepts used:

1.	File Handling (Open, read, write)
2.  Lists for raw data storage
3.	Sets for duplicate removal
4.	Dictionaries for structured mapping
5.	String methods for normalization
6.	enumerate for roll number assignment


How to Run the Project:

1. Clone the repository to local system.
2. Run main.py using Python 3 or above

Requirements: 
1. Python 3 or above
2. No external requirements


Future Improvements:

1.	Read data from CSV files
2.	Add proper exception handling
3.	Add unit tests
4.	Support larger datasets efficiently.