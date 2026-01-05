"""
Countings Vowels in a String
- A function to count the number of vowels (a, e, i, o, u)both upper and lowercase
in a given string. 
"""

# Function to count vowels
def count_vowels(s):
    """Return the number of vowels in string s."""
    vowels = "aeiouAEIOU"
    # generator expression inside sum()
    return sum(1 for char in s if char in vowels)

# Testing with sample predefined word 'Programming'
print(count_vowels("Programming"))
