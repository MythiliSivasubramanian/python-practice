print("=== Max & Min Finder ===")

while True:
    data = input("Enter numbers separated by commas: ")

    try:
        numbers = [float(x.strip()) for x in data.split(",")]
        print(f"Maximum value: {max(numbers)}")
        print(f"Minimum value: {min(numbers)}")
    except ValueError:
        print("Please enter valid numbers only.")
        continue

    again = input("Analyze another list? (y/n): ").lower()
    if again != "y":
        break
