""" Count words that start with a vowel in a sentence . Counts how many words start with a vowel (a, e, i, o, u)
Ignore case Sample Input: I am learning Python and it is fun . Sample Output : Words starting with a vowel: 5 """

user_string = input("Enter a string : ").lower().split()
vowels = "aeiou"
count = 0

for word in user_string:
    if word and word[0] in vowels:
        count += 1

print("Words starting with a vowel:", count)

