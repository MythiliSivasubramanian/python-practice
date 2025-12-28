#Get the sentence as a string and print the total occurances of each word 
def word_frequency(sentence):

    freq = {}
    words = sentence.lower().split() # Converted all cases of word to lower 

    for w in words:
         # increment count if word exists, otherwise start from 1
        freq[w] = freq.get(w, 0) + 1

    return freq

# Get the input
user_input = input("Enter a Sentence to count each word frequency : ")

# Call the fun(). Pass input and assign return value to word_count
word_count = word_frequency(user_input)

# Print result
print(word_count)
