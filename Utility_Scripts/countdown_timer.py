import time

print("=== Countdown Timer ===")

while True:
    try:
        seconds = int(input("Enter number of seconds: "))
        if seconds <= 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    print("Starting countdown...")
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

    again = input("Run another timer? (y/n): ").lower()
    if again != "y":
        break
