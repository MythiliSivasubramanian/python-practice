"""Remove all characters from a string except alphabets (A–Z, a–z). Sample Input : 1. Pyth0n! is aw3s0me!! 2. 123@#Hello!!
Sample Output: 1. Pythonisawesome   2. Hello """

user_string = input("Enter a String : ")
processed_string = ""
for char in user_string:
    if char.isalpha():
        processed_string += char
print(processed_string)
