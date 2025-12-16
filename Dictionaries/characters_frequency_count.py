# Count the frequency of each characters (including spaces) from the given string input

# Get the input
text = input("Enter a string to count frequency of each character : ")

# Create a empty dict() to store charcters and thier occurences as pairs
count = {}

# Read each char from the string and char as key and its count as value in count{}
for char in text:
    count[char] = count.get(char,0) + 1
print(count)
