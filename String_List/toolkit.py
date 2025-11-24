def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(ch in vowels for ch in s)

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

def is_palindrome(s):
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_clean == s_clean[::-1]

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
