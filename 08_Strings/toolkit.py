"""
String Utilities Program :
1. Reversing a string
2. Counting vowels in a string
3. Finding the longest word in a sentence
4. Calculating frequency of words
5. Checking if a string is a palindrome
6. Demonstrating case operations
"""

# Returns the reverse of the string 's'.
def reverse_string(s):
    return s[::-1]

# Returns the number of vowels in the string s.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(ch in vowels for ch in s)


# Returns the longest word in the sentence. Returns empty string if no words.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

# Returns dictionary with frequency of each word in the sentence.
def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split(): # Converting to lower case and spliting
        freq[word] = freq.get(word, 0) + 1
    return freq

# Checking if 's' is a palindrome.
def is_palindrome(s):
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]

# Different cases on the string. Returns dictionary with 'lower' and 'casefold' conversions.

def case_demo(s):
    return {"lower": s.lower(), "casefold": s.casefold()}

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Reversed:", reverse_string(text))
    print("Vowel Count:", count_vowels(text))
    print("Longest Word:", longest_word(text))
    print("Word Frequency:", word_frequency(text))
    print("Palindrome:", is_palindrome(text))
    print("Case Comparison:", case_demo(text))
