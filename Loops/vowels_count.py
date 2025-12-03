# Countr vowels in a string 

text = input("Enter a string : ")
vowels = "aeiou"
count = 0

for ch in text:
    if ch.lower() in vowels:
        count += 1

print("Number of vowels:", count)
