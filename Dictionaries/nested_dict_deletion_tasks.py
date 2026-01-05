"""
Nested Dictionary:
- Creation of nested dictionary
- Inner dictionary key deletion using del and pop()
- Safely removing entire inner dictionary using pop()
- Clearing inner dictionary using clear()
- Deleting multiple keys from inner dictionary+
- Removing outer dictionary keys
"""

# Creating a nested dictionary
student = { "name": "Rose", "marks": {"math": 98, "cs": 99, "physics": 92},"address": {"city": "Hamburg", "country": "Germany", "pincode": 12345}}
print(f"\nInitial Nested Dictionary:\n{student}")


# Deleting the key 'cs' from inner dictionary 'marks using del'
print("\nDeleting the key 'cs' from inner dictionary 'marks' : \nStep 1: del student['marks']['cs'] : " )
del student["marks"]["cs"]
print(student)

# Deleting the inner dictionary key 'physics' from 'marks'and printing the removed value
print("\nDeleting the inner dictionary key 'physics' and printing the removed value : \n")
removed_value = student["marks"].pop("physics","Key not found")
print("Removed Value is : ",removed_value,"\nUpdated dictionary : ",student)

# Removing the entire "address" inner dictionary safely
print("\nRemoving the entire 'address' dictionary safely : ")
removed = student.pop("address","key not found")
print("Removed values : ",removed,"\nupdated dictionary : ",student)

# Clearing an inner dictionary
print("\nClearing an inner dictionary using .clear() : ")
student["marks"].clear()
print("updated dictionary : ",student)

# Deleting multiple keys from nested dictionary
student = { "name": "Rose", "marks": {"math": 98, "cs": 99, "physics": 92},"address": {"city": "Hamburg", "country": "Germany", "pincode": 12345}}
print("Deleting multiple keys from nested dictionary : \nInitial dictionary is : ",student)
to_remove = ["city","country"]

for k in list(student["address"]):
    if k in to_remove:
        del student["address"][k]
print("\n\nUpdated dictionary is :\n",student)
    

# Removing a key safely with .pop() and storing removed values in a list
student = { "name": "Rose", "marks": {"math": 98, "cs": 99, "physics": 92},"address": {"city": "Hamburg", "country": "Germany", "pincode": 12345}}
print("\nInitial dictionary is : ",student)
key_to_remove = ["city","country","pincode"]

removed_values = []
for k in list(student["address"]):
    if k in key_to_remove:
        removed_values.append(student["address"].pop(k))
print("\nRemoved Value is : ",removed_values)
print("\nFinal Dictionary after removing keys from inner dictionary is : \n",student)

# Deleting outer dictionary keys using del. marks
del student["marks"]
print("\nDeleting outer dictionary keys 'marks' using del : \n",student )

# Removing the last key-value pair.
removed_pair = student.popitem()
print("\nRemoving the last key-value pair, which is : ",removed_pair)
print("\nUpdated Dictionary is : ",student)
