# To remove duplicates items in the list

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

items = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", items)
print("After removing duplicates:", remove_duplicates(items))
