# Program to replace spaces with underscores

def replace_spaces(text):
    return text.replace(" ", "_")


# Test the function
if __name__ == "__main__":
    sentence = "Python string practice"
    print("Modified string:", replace_spaces(sentence))
