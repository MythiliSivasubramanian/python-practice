# find_index.py
# Program to find the index of an element in a list without using index()

def find_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

if __name__ == "__main__":
    items = ["apple", "banana", "cherry", "date"]
    value = "cherry"
    print("List:", items)
    print(f"Index of '{value}':", find_index(items, value))
