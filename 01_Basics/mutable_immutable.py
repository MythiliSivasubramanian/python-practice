import sys

# Immutable object
a = 10
b = a
print("Before change:")
print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))

a += 5  # Creates new int object
print("\nAfter a += 5:")
print("a:", a, "id:", id(a))
print("b:", b, "id:", id(b))  # b still references old object

# Mutable object
x = [1, 2, 3]
y = x
print("\nBefore mutation:")
print("x:", x, "id:", id(x))
print("y:", y, "id:", id(y))

x.append(4)  # Mutates object in-place
print("\nAfter x.append(4):")
print("x:", x, "id:", id(x))
print("y:", y, "id:", id(y))  # y sees the change because same object
