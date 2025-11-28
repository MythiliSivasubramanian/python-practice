""" Given " python ", trim spaces on both sides. Sample Input: " python " → Output: "python"""
import string

user_inoput = input("Enter a word with spaces on front and at end : ")
print(f"After trimming spaces from front and back end : {user_inoput.strip(string.whitespace)}")
