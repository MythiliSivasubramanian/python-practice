# Count vowels and consonants in a string

def count_vowels_consonants(text):
    # Both upper and lower case vowels 
    vowels = "aeiouAEIOU"

    # Inital count of vowels (both cases) as 0
    vowels_count = 0

    # Inital count of consonants as 0
    consonants_count = 0

    for char in text:
        # .isalpha() considers only alphabetic characters
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count

# Testing the function with sample string
print(count_vowels_consonants("Test Message"))
