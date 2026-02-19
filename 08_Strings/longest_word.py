""" Find the longest word in a string. sample Input: "I love programming in Python"
Sample Output: programming """

user_string = input("Enter a string separated by space: ").split(" ")
print(max(user_string,key= len))
