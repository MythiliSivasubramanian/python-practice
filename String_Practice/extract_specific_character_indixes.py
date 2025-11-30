
""" Given "Programming", extract: The first 3 letters , The last 4 letters ,Every second character
Sample Input: "Programming"
Sample Output: First 3 letters: Pro
Last 4 letters: ming
Every second character: Pormig """
user_text = input("Enter a Word : ")
n = 4
print(f"First 3 letters: {user_text[0:3]}\nLast 4 letters: {user_text[-n:]}\nEvery second character : {user_text[::2]}")
