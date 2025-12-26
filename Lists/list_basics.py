# Printing each number squared

# Initial list
numbers = [5, 2, 9, 1, 7]
print("\nInital list is : ",numbers)

# A empty list to store the squared numbers
squared = []

# Read each item in the list using for loop and compute squared of each item
for num in numbers:
    squared.append(num * num)
print("\nSquared of each item in the list :\n",squared)


# Checking if the number 3 and 7 is in numbers or squared list
# Returns True if the number is in any of the list.
print(3 in numbers or 3 in squared)
print(7 in numbers or 7 in squared) 

# Sorting the list in ascending order and print it.
numbers.sort(reverse = False)
print("Sorting the list in ascending order : ",numbers)

# Sorting the list in descending order and print it.
numbers.sort(reverse = True)
print("\nSorting the list in descending order : ",numbers)

# Combing list 1 and list 2
# Method 1 : using +

combined_list = numbers + squared
print("\nCombined list with numbers and squared using + is : \n",numbers + squared)

# Method 2 : using .extend
numbers.extend(squared)
print("\nCombined list numbers and squared using .extend() is : \n",numbers)
