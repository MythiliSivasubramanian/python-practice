""" Count how many times "a" appears in "abracadabra". Sample Input: "abracadabra".
Sample Output: 5 """

# Method 1 : Using count()

user_input = input("Enter a Word or a String : ")
search_char = input("Enter the Character or Symbol to search in the String : ")
print(user_input.count(search_char))

# Method 2 : using loop (manual)

count = 0
for ch in user_input:
    if ch == search_char:
        count += 1
print(count)

