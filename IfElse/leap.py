"""
Leap Year Checker :
Checking whether a given year is a leap year.
Leap year if :
- Year divisible by 4 but not by 100, OR
- Year divisible by 400
"""

# Prompting the user to enter a year
year = int(input("Enter a year: "))

# Checking leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
