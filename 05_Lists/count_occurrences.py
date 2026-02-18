# Program to count how many times each element appears in a list

def count_occurrences(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == "__main__":
    words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
    print("List:", words)
    print("Occurrences:", count_occurrences(words))
