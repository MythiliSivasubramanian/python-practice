""" To Check if two strings are anagrams of each other. Two strings are anagrams if:
They have the same characters , With the same frequency but Order does not matter
Sample Input: 1. listen ,silent 2. hello , bello  Sample Output: 1. True  2. False """

# Method 1 : Using dictionary()

user_input_1 = input("Enter 1st word : ").lower()
user_input_2 = input("Enter 2nd word : ").lower()

count_1 = {}
count_2 = {}

for char in user_input_1:
    count_1[char] = count_1.get(char,0) + 1

for char in user_input_2:
    count_2[char] = count_2.get(char,0) + 1

print(count_1 == count_2)


# Method 2: Using sort()

print(sorted(user_input_1)==sorted(user_input_2))
