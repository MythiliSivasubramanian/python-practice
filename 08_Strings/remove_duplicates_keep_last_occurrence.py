"""Given a string, remove all duplicate characters but keep the last occurrence of each character.
Sample Input: "abracadabra" Sample  Output: rcdba """

user_string = input("Enter a string: ")
seen = set()
result = []

# Traverse LEFT → RIGHT
for char in user_string:
    # remove previous occurrence if exists
    if char in seen:
        result.remove(char)
    seen.add(char)
    result.append(char)

output = "".join(result)
print(output)
