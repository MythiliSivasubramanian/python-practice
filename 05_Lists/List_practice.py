"""
File: list_practice.py
Topic: Python Lists Basics

Concepts covered:
- List creation
- Indexing (positive & negative)
- Length calculation
- Append operation
- Update exsisting item in list

"""




"""
Task 1 — Create & Print 
Create a list of 5 fruits and:
Print the whole list,  first fruit, last fruit

"""

# Create a List with 5 fruits
my_fruits = ["Apple", "Orange", "Kiwi", "Mango", "Grapes"]

# Print whole list
print("\nPrinting the whole list of my_fruits :\n", my_fruits)

# Accessimg the item in a list.
# Print the first fruit (1st item in list)
print("\nFirst fruit in the list is :", my_fruits[0]) 

# Print last fruits in list
print("\nLast fruit in list is :", my_fruits[-1])

# Print 2nd fruit
print("\n2nd Fruit is :", my_fruits[1])

# Print 2nd last fruit
print("\n2nd Last Fruit is :", my_fruits[-2])

# Add "Pineapple" to  fruits list and print updated list.
# Append adds the item at the end of list. .instert(index,item) will add item at specified index
my_fruits.append("Pineapple")
print("\nUpdated list is :", my_fruits)

# Replace "Kiwi" with "Strawberry".
my_fruits[2] = "Strawberry"
print("\nUpdated list is :", my_fruits)

"""
Task 2 — Length Check : Create a list of numbers: [10, 20, 30, 40, 50, 60]
Print the list length and Print the 3rd element
"""

# Create a list with 10, 20, 30, 40, 50, 60
my_list = [10, 20, 30, 40, 50, 60]

# Print the length of the list
print("\nLength of my_list is : ",len(my_list))

# Access 3rd item in list. Index starts from 0
# Print 3rd element in list
print("\n3rd Element in my_list is : ",my_list[2])

"""
Task 3 — Change Values
Given: colors = ["red", "blue", "green", "yellow"]
Change "blue" → "black" and Print updated list
"""

# Predefined list
colors = ["red", "blue", "green", "yellow"]

# Update existing value in list
# Change 'blue' as 'black'
print("\nOriginal List is : \n",colors)

# Lists are mutable. Lists can be modified in-place.
colors[1] = 'black'

# Print the new list with updated value
print("\nUpdated list is : \n",colors)

