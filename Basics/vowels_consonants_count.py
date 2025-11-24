# Count vowels and consonants in a string

def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count

print(count_vowels_consonants("Test Message"))
