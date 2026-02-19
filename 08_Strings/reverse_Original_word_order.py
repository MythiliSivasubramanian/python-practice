"""Reverse each word in a sentence but keep the word order the same
Sample Input: I love Python . Sample Output: I evol nohtyP """

my_string = input("Enter the String : ").split(" ")
new_list = []
for word in my_string:
    new_list.append(word[::-1])
print(" ".join(new_list))
