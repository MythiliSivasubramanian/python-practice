"""Join a list of words into a sentence. Sample Input: ['I', 'love', 'Python']
Sample Output: I love Python """

# .split() returns class type list of a input string
user_string = input("Enter a items in list separated by comma : ").split(",")

# join() is used to convert list to string type with spaces
print(" ".join(user_string))
