""" Given a string, count: Number of consonants, 
Number of digits,Number of spaces Number of special characters (anything that is not letter/digit/space)"""



consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
numbers = "0123456789"

consonants_count = 0
numbers_count = 0
special_chars_count = 0
space = " "
space_count = 0

user_input = input("Enter a String : ")

for ch in user_input:
    if ch in consonants:
        consonants_count += 1
    elif ch in numbers:
        numbers_count += 1
    elif ch in space:
        space_count += 1
    else:
        special_chars_count += 1
        
print(f"consonants = {consonants_count}\nnumbers = {numbers_count}\nspace : {space_count}\nspecial_chars = {special_chars_count}")
        
    
