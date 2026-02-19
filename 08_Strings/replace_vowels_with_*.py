""" Replace all vowels in a string with "*"   Sample Input: "Hello World". Sample Output: H*ll* W*rld """

# Method 1:  Using for loop ()
user_text = input("Enter a String with Vowels (eg: Hello World) : ")
vowels = "aeiouAEIOU"
masked_text =""
for i in user_text:
    if i not in vowels:
        masked_text += i
    else:
        masked_text += "*"
print(masked_text)

# Method 2 : short version using replace()
masked_char = "*"
for vowel in vowels:
    user_text = user_text.replace(vowel,masked_char)
print(user_text)

