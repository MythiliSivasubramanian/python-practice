# To count how many vowels (a, e, i, o, u — both upper and lower case) are in a given string. Withoiut using count()

vowels = "aeiouAEIOU"
user_string = input("Enter a Word : ")

vowels_count = 0

for char in user_string:
    if char in vowels:
        vowels_count += 1
   
print("Count is : ",vowels_count)
