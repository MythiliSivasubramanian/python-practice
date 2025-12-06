def count_vowels(s):
    """Return the number of vowels in string s."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Programming"))
