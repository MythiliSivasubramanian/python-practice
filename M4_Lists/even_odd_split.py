# To split even and odd from a list

def split_even_odd(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return even, odd

numbers = [10, 15, 22, 33, 42, 57, 60]
even_numbers, odd_numbers = split_even_odd(numbers)
print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
