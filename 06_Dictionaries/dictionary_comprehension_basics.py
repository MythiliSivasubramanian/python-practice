# Dictionary Comprehension 
# Creating a dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} Keys are n*n)

# Method 1: Using for loop
d = {} # Empty dictionary
for i in range(1, 6):
    d[i] = i * i

print("Dictionary using for loop:", d)

# Method 2: Using dictionary comprehension
d = {i: i * i for i in range(1, 6)}
print("Dictionary using dict comprehension:", d)
