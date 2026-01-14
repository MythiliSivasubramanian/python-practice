#  Union of two sets from user input

# Get the elements of 2 sets from user (Valus separated by comma)
set1 = set(input("Enter first set values (comma separated): ").split(","))
set2 = set(input("Enter second set values (comma separated): ").split(","))

# Union is set1 + set2 without duplicates. Sets doesnt allow duplicates. 
union_result = set1 | set2

print("\n Set 1 : ", set1)
print("\n Set 2 : ", set2)
print("\n Union : set1 | set2 : ", union_result)
print("\n Total unique elements : ", len(union_result))