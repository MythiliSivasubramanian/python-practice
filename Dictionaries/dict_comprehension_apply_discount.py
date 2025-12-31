""" Creating a new dictionary by applying a discount to each item in an existing price dictionary 
using dictionary comprehension """

# Original price dictionary
prices = {
    "apple": 100,
    "banana": 40,
    "cherry": 150
}

# Dictionary comprehension:
# - iterating over key-value pairs using .items() and subtracting 10 from each item's price

discounted = {item: price - 10 for item, price in prices.items()}

# Print original and discounted prices
print("\nOriginal prices:", prices)
print("\nDiscounted prices:", discounted)
