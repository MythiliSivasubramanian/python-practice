# Union of words from two sentences

# Sentence1 and sentence2
sentence1 = "python is easy and powerful"
sentence2 = "python is powerful and fun"

# Converting string of sentence to sets
set1 = set(sentence1.split())
set2 = set(sentence2.split())

# union of set1 and set2 . Sets doesnt allow duplicates
all_words = set1.union(set2)

# Printing the results
print("\nSentence 1 words:", set1)
print("\n Sentence 2 words:", set2)
print("\n All unique words:", all_words)
