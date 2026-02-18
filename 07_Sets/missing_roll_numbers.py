# Find missing roll numbers

all_rolls = set(range(1, 11))      # Numbers from 1 to 10
present_rolls = {1, 2, 3, 5, 6, 8}

missing = all_rolls - present_rolls

print("\nAll Rolls : ", all_rolls)
print("\nPresent Rolls : ", present_rolls)
print("\nMissing Rolls : ", missing)