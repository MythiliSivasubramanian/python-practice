""" 
Python Sets Basics
- Creating sets
- Adding and removing elements
- Removing duplicates using sets
- Membership checking

-  To Understand that sets store UNIQUE values
- basic set operations and behavior
"""

# Create a set, add and remove elements
numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

numbers.add(6)          # add a single element
numbers.remove(3)       # remove an existing element
print("Updated set:", numbers)


# Remove duplicates from a list using set
nums = [1, 2, 2, 3, 4, 4, 5]

unique_nums = set(nums)        # removes duplicates
unique_list = list(unique_nums)

print("List without duplicates:", unique_list)


# Membership check
fruits = {"apple", "banana", "orange"}

user_fruit = input("Enter a fruit: ")

if user_fruit in fruits:
    print("Fruit exists in the set")
else:
    print("Fruit does NOT exist in the set")
