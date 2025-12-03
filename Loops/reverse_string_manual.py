#Reverse the string

text = input("Enter a word: ")
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print("Reversed:", reversed_text)
