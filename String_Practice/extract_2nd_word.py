""" Given two words as input, extract only the second word after space.
Sample Input : 1. Hello World              2. Good Morning                 
Sample output: 1. World                       2. Morning

# Method 1 : Using split() und list
user_input = input("Enter 2 words : ")
words_list = list(user_input.split(" "))
print(words_list[1])

# Method 2 : Using indexing
second_word = user_input[user_input.find(" ") + 1:]
print(second_word)


