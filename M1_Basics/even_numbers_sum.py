# Sum only even numbers in a list

def sum_even_numbers(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
