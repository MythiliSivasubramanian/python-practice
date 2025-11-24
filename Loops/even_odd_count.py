# To count even, odd numbers in a list
def count_even_odd(numbers):
    even,odd = 0,0  

    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))

    even_count, odd_count = count_even_odd(nums)

    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
