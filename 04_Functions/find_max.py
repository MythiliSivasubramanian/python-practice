"""
Finding Maximum in a List
A function to find the largest number in a given list.
"""

# Function to find maximum number
def find_max(numbers):
    """Return the highest number from a list."""
    if not numbers:
        raise ValueError("The list is empty.")
    
    # Assuming initially the first element as the largest 
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Testing the logic
print("\nFinding the largest number from the list [3, 8, 2, 10, 6] : ")
print(find_max([3, 8, 2, 10, 6]))