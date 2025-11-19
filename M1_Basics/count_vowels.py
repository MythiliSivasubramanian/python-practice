# Count vowels in a given string

def count_vowels(text):
    vowels = input("Enter a string")
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print(count_vowels())
