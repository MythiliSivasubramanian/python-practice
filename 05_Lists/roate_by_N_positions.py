#Rotate a list by N positions
def rotate_list(lst, n):
    n = n % len(lst)  # Handle n > len(lst)
    return lst[-n:] + lst[:-n]

numbers = [1, 2, 3, 4, 5]
rotated = rotate_list(numbers, 2)
print("Rotated list by 2 positions:", rotated)
