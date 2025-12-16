# Count vowels in a given string

def count_vowels():
    text = input("Enter a string to count the vowels in it : ")
    count = 0
    vowels = "AEIOUaeiou" # vowels 

    for char in text:
        if char in vowels:
            count += 1
    return count

# Call the function and asssign the return value of the fun() to a variable
vowels_count = count_vowels()

# Print result
print(F"Vowels count is : {vowels_count}")

