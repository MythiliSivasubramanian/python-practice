# Program to find the second largest number in a list

def second_largest(numbers):
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

if __name__ == "__main__":
    nums = [10, 20, 4, 45, 99, 45]
    print("Numbers:", nums)
    print("Second largest:", second_largest(nums))
