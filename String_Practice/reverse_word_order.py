""" Reverse the order of words in a sentence.  Sample Input: "I love Python programming" Sample Output:
programming Python love I """

user_string = input("Enter the string : ").split(" ")
reversed_string = user_string[::-1]
print(" ".join(reversed_string))

# Or

user_string = input("Enter the string: ").split()
print(" ".join(user_string[::-1]))
