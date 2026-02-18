# Count occurrences of each element
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {fruit: fruits.count(fruit) for fruit in set(fruits)}
print("Element counts:", counts)
