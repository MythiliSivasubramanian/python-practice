"""
Word Frequency Counter :
Counting how many times each word appears in a sentence.
Ignoring case.
"""

import string

print("=== Word Frequency Counter ===")

# Prompting the user to enter the input
sentence = input("Enter a sentence: ").lower()
# Spliting sentence into words using split()
words = sentence.split()

# Creating a empty dictionary : Frequency dictionary
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("\nWord Frequency:")
for word, count in freq.items():
    print(f"{word}: {count}")
