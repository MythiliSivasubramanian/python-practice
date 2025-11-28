""" Given a string, remove all duplicate characters while keeping only the first occurrence of each character.
Sample Input: bananas.  Sample Output: bans """


user_input = input("Enter a Word : ")

# Method 1 : Using dict.fromkeys()
print("".join(dict.fromkeys(user_input)))

# Method 2: Using OrderedDict.fromkeys()
print("".join(OrderedDict.fromkeys(user_input)))

# Method 3: Using for Loop with a Set
processed_word = set()
cleaned_word = ""
for char in user_input:
    if char not in processed_word:
        processed_word.add(char)
        cleaned_word += char
print(cleaned_word)


# Method 4 : Using List Comprehension with Slicing
print("".join([char for i, char in enumerate(user_input) if char not in user_input[:i]]))

