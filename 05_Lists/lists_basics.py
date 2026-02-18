my_fruits = ["apple","banana","cherry"]
print("\nInitial list is : ",my_fruits)

# Printing the 1st item in the list
print("Printing the 1st item in the list : ",my_fruits[0])

# Printing the last item in the list
print("\nPrinting the last item in the list : ",my_fruits[-1])

# Updating "banana" to "blueberry" in your list 
my_fruits[1] = "blueberry"
print("\nUpdating 'banana' to 'blueberry' in your list  : \nUpdated list is : ",my_fruits)

# Adding items to the list. Orange at the end of the list and Kiwi at the start
my_fruits.append("Orange") # .append() adds the item at the end of the list
my_fruits.insert(0,"kiwi") # .insert() add the item at the specified position 
print("\nAdded Orange at end and kiwi at 1st : \nUpdated list is : ",my_fruits)

# Remove cherry by value
my_fruits.remove("cherry") 
print("\nRemoving cherry by its index value : \nUpdated list is : ",my_fruits)

# Printing the first 3 fruits
print("Printing the first 3 fruits : ",my_fruits[:3])

# Printing last 3 fruits
print("\nPrinting last 3 fruits : ",my_fruits[-2:])
