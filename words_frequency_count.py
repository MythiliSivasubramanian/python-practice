""" Frequency Counter : Given the string:Count the frequency of each word in the string and store it in a dictionary. 
Sample Input: "Python is fun and Python is powerful" 
Sample Output: {'Python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1} """


# Get the input and split into a list based on spaces
my_string = input("Enter a sentence to count the words frequency: ").split()

# Create an empty dictionary
word_frequency = {}

# Count each word
for word in my_string:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Print the frequency dictionary
print(word_frequency)
