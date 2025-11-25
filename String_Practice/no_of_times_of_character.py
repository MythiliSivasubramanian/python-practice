
""" Count how many times each character appears in a string.
Sample Input: banana  Sample Output:
b → 1
a → 3
n → 2 """

user_input = input("Enter a word : ")
char_count = {}

for ch in user_input:
    if ch not in char_count:
        char_count[ch] = 1
    else:
        char_count[ch] += 1

for ch,count in char_count.items():
    print(ch,"--", count)
