
# Count frequency of each character from the given input AND sort them by last occurrence.

my_string = input("Enter a Word : ")

# Store the count of each characters
count = {}
for char in my_string:
    count[char] = count.get(char,0) + 1


# Find the last index
last_index = {}
for index, char in enumerate(my_string):
    last_index[char] = index


# Sort the order

sorted_chars = sorted(last_index,key = lambda x: last_index[x],reverse = True)

# Print the result
for char in sorted_chars:
    print(f"{char} → {count[char]}")
