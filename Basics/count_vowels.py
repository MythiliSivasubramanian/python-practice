# Count vowels in a given string

def count_vowels():
    # get the input string
    text = input("Enter a string to count the vowels in it : ") 
    count = 0 # Initial count of vowels is 0
    vowels = "AEIOUaeiou" #  # includes both uppercase and lowercase vowels 

    # Loop to count the vowels from the input 'text'
    for char in text:
        if char in vowels:
            count += 1
            # return total number of vowels found
    return count

# Call the function and asssign the return value of the fun() to a variable
vowels_count = count_vowels()

# Print result
print(f"Vowels count is : {vowels_count}")

