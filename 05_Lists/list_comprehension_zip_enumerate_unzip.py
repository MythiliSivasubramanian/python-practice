"""
Practice: 
- list comprehension
- zip and unzip
- enumerate
- filtering data
- formatting output with f-strings
"""

# Predefined lists
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
prices = [1200, 25, 75, 300]

# Step 1: Zip products and prices
product_price = list(zip(products, prices))
print("Zipped product-price list:")
print(product_price, "\n")

# Step 2 + Step 3: Enumerate + list comprehension + filtering
# Create formatted strings only for products costing more than 100
costly_products_report = [
    f"{index}. {product} costs {price}"
    for index, (product, price) in enumerate(product_price, start=1)
    if price > 100
]

print("Products costing more than 100:")
for line in costly_products_report:
    print(line)

# Step 4: Unzip back into separate lists
items, costs = zip(*product_price)

# Convert tuples to lists
items = list(items)
costs = list(costs)

print("\nUnzipped lists:")
print("Items:", items)
print("Costs:", costs)
