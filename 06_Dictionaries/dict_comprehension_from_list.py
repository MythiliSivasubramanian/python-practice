# Creating dictionary using dict comprehension from predefined list

numbers_list = [1,2,3,4,5]
print("\nThe predefined list is : ",numbers_list)

print("\nCreating a dictionary from the predefined list using dictionary comprehension - keys are double the numbers :\n")
my_dictionary = {x: x*2 for x in numbers_list}
print(my_dictionary)
