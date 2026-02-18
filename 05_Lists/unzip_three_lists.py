# Unzip three lists into individual lists

# Predefined list of tuples
student_info = [('Alice', 24, 'USA'), ('Bob', 30, 'UK'), ('Charlie', 22, 'Canada')]

names,ages,countries = zip(*student_info)
print(names,ages,countries)

# Convert the results from tuples to lists
names = list(names)
ages = list(ages)
countries = list(countries)

print("\nList of names is : ",names)
print("\nList of ages is : ",ages)
print("\nList of countries is : ",countries)
