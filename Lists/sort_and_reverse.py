# Program to sort a list in ascending and descending order and then reverse it manually

def sort_and_reverse_list(numbers):
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    manual_reverse = []
    for i in range(len(numbers) - 1, -1, -1):
        manual_reverse.append(numbers[i])
    return ascending, descending, manual_reverse


numbers = [5, 3, 8, 1, 2, 7]
asc, desc, manual_rev = sort_and_reverse_list(numbers)
print("Original list:", numbers)
print("Sorted (Ascending):", asc)
print("Sorted (Descending):", desc)
print("Manually Reversed:", manual_rev)
