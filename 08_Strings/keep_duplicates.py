"""Given a string, keep only the characters that appear more than once,but keep only their first occurrence in the output.
Sample Input :  mississippi Sample outpu    t : isp """


user_word = input("Enter a word : ")

count_dict = dict()
result = ""
seen_word= set()
for char in user_word:
    count_dict[char] = count_dict.get(char,0) + 1
print(count_dict)

for char in user_word:
    if count_dict[char] > 1:
        seen_word += char
print(seen_word)
