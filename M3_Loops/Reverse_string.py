# To Reverse a string
def reverse_string(text):
    reversed_text = ""  
    i = len(text) - 1   

    while i >= 0:
        reversed_text += text[i]
        i -= 1
    return reversed_text


if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Reversed string:", reverse_string(s))
