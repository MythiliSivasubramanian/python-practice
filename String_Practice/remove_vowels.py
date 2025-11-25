""" Remove all vowels from a string. Sample Input: beautiful day Sample Output: btfl dy"""

vowels = "AEIOUaeiou"
user_input = input("Enter a word or string : ")
cleaned_word = ""
for ch in user_input:
    if ch not in vowels:
        cleaned_word += ch
    
print(cleaned_word)
