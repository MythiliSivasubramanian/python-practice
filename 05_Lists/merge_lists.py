# Program to merge two lists without using + operator or extend()

def merge_lists(list1, list2):
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("List 1:", a)
    print("List 2:", b)
    print("Merged list:", merge_lists(a, b))
