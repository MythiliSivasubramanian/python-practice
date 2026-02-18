# Word frequency counter. 
# Given a string, count the frequency of each word using a dictionary.

# Sample sentence
sentence = "python is easy and python is powerful"
print("\nPredefined sample sentence : \n",sentence)
# Split the sentence into words using split()
words = sentence.split()

# Creating a empty dict to store the word counts
frequency = {}

# Count the frequency of words using for loop
for word in words:
    if word in frequency:
        # Increment by 1 if word exists 
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequency : \n",frequency)
