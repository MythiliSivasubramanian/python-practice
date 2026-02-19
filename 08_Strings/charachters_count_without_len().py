
""" Count how many characters are in a string without using len().
Sample Input: Python Output: 6 """

# Method 1 : using for loop (manual)
user_input = input("Enter a String or a Word : ")
counter = 0
for i in user_input:
    counter += 1
print(counter)

# Method 2: using count():
print(user_input.count("")-1)

# Method 3 : Using enumerate ()
count = 0
for i, ch in enumerate(user_input):
    count += 1
print(count)
  
