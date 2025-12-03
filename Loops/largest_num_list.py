# Find largest number in the given list

numbers = [12, 5, 29, 3, 18]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)
