"""
Vowel or Consonant Checker:
Checking whether the entered character is a vowel or consonant.
"""
# Prompt user to enter a character and changing to lower case
ch = input("Enter a character: ").lower()

# Validating input
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
