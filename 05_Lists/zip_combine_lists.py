# Combining two lists with different lengths

"""
Two lists: A list of names (names) and A list of ages (ages)
Create a list of tuples, pairing each name with the corresponding age. But, one of the lists may be longer than the other.
"""

# Predefined lists
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 30]


# If the lists have different lengths, zip() will stop when the shortest list is exhausted.
data = list(zip(names,ages))
print("\nIf the lists have different lengths, zip() will stop when the shortest list is exhausted \nList with names and ages : ",data)
