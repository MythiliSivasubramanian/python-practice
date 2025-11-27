"""Find the second largest number in a list. Sample Input: [4, 7, 1, 9, 5] Sample Output: Second largest: 7 """


def find_second_largest(nums):
    if len(nums) < 2:
        return None

    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second


def get_input(prompt, error_message):
    while True:
        try:
            return list(map(float, input(prompt).split(",")))
        except ValueError:
            print(error_message)


def main():
    prompt = "Enter numbers separated by commas (e.g., 3,-2,0,5.5): "
    error = "Invalid input—please enter valid numbers."

    user_list = get_input(prompt, error)

    # Method 1
    second_largest = find_second_largest(user_list)
    print(f"Method 1 → Second largest: {second_largest}")

    # Method 2
    ordered = sorted(user_list)
    print(f"Method 2 → Second largest: {ordered[-2]}")


if __name__ == "__main__":
    main()
