""" Count the number of vowels and consonants in a string . Ignore spaces, digits, and special characters.
Sample Input: Python is fun .  Sample Output: Vowels: 3 Consonants: 8 """

vowels = "AEIOUaeiou"
user_input = input("Enter a String : ")
vowels_count = 0
consonants_count = 0

for char in user_input:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonants_count += 1
print(f"Vowels : {vowels_count} Consonants : {consonants_count}")


