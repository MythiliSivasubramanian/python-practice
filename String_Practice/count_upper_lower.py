# Program to count uppercase and lowercase letters

def count_upper_lower(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


# Test the function
if __name__ == "__main__":
    sentence = "Python Is Fun"
    upper, lower = count_upper_lower(sentence)
    print("Uppercase:", upper)
    print("Lowercase:", lower)
