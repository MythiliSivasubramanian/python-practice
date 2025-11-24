# Find duplicate values in a list

def find_duplicates(nums):
    seen = []
    duplicates = []

    for n in nums:
        if n in seen and n not in duplicates:
            duplicates.append(n)
        else:
            seen.append(n)

    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))
